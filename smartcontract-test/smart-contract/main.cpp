#include "contract_clean.h"

// Global contract state instance
CONTRACT_STATE contractState;
QubicContext qubicContext;

// Initialize the contract
void initializeContract() {
    contractState.totalVotes = 0;
    contractState.totalProposals = 0;
    contractState.totalRegisteredVoters = 0;
    contractState.contractCreationTime = getCurrentTime();
    contractState.isActive = true;
    
    // Initialize arrays
    for (int i = 0; i < MAX_VOTES; i++) {
        contractState.votes[i].isValid = false;
        contractState.voters[i].isRegistered = false;
    }
    
    for (int i = 0; i < MAX_PROPOSALS; i++) {
        contractState.proposals[i].isActive = false;
    }
}

// Create a new proposal
unsigned int createProposal(const char* title, const char* description, unsigned long long duration) {
    if (contractState.totalProposals >= MAX_PROPOSALS) {
        return 0; // Failed: too many proposals
    }
    
    unsigned int proposalId = contractState.totalProposals + 1;
    Proposal* proposal = &contractState.proposals[contractState.totalProposals];
    
    proposal->id = proposalId;
    copyString(proposal->title, title, sizeof(proposal->title));
    copyString(proposal->description, description, sizeof(proposal->description));
    proposal->startTime = getCurrentTime();
    proposal->endTime = proposal->startTime + duration;
    proposal->yesVotes = 0;
    proposal->noVotes = 0;
    proposal->abstainVotes = 0;
    proposal->status = ACTIVE;
    proposal->isActive = true;
    
    contractState.totalProposals++;
    return proposalId;
}

// Register a voter
bool registerVoter(const char* userId) {
    if (contractState.totalRegisteredVoters >= MAX_VOTES) {
        return false; // Too many voters
    }
    
    // Check if voter already registered
    if (isVoterRegistered(userId)) {
        return false; // Already registered
    }
    
    Voter* voter = &contractState.voters[contractState.totalRegisteredVoters];
    copyString(voter->userId, userId, sizeof(voter->userId));
    voter->isRegistered = true;
    voter->reputation = 100; // Initial reputation
    voter->registrationTime = getCurrentTime();
    
    contractState.totalRegisteredVoters++;
    return true;
}

// Cast a vote
bool castVote(unsigned int proposalId, const char* userId, VoteChoice choice, const char* comment) {
    if (!isValidProposal(proposalId)) {
        return false;
    }
    
    if (!isProposalActive(proposalId)) {
        return false;
    }
    
    if (!isVoterRegistered(userId)) {
        return false;
    }
    
    if (hasVoterVoted(proposalId, userId)) {
        return false; // Already voted
    }
    
    if (contractState.totalVotes >= MAX_VOTES) {
        return false; // Too many votes
    }
    
    Vote* vote = &contractState.votes[contractState.totalVotes];
    vote->proposalId = proposalId;
    copyString(vote->userId, userId, sizeof(vote->userId));
    vote->choice = choice;
    copyString(vote->comment, comment, sizeof(vote->comment));
    vote->timestamp = getCurrentTime();
    vote->voteWeight = 1; // Simple 1-vote-per-person for now
    vote->isValid = true;
    
    contractState.totalVotes++;
    
    // Update proposal vote counts
    updateProposalVoteCounts(proposalId);
    
    return true;
}

// Update proposal vote counts
void updateProposalVoteCounts(unsigned int proposalId) {
    if (!isValidProposal(proposalId)) return;
    
    Proposal* proposal = &contractState.proposals[proposalId - 1];
    proposal->yesVotes = 0;
    proposal->noVotes = 0;
    proposal->abstainVotes = 0;
    
    for (int i = 0; i < contractState.totalVotes; i++) {
        Vote* vote = &contractState.votes[i];
        if (vote->isValid && vote->proposalId == proposalId) {
            switch (vote->choice) {
                case VOTE_YES:
                    proposal->yesVotes++;
                    break;
                case VOTE_NO:
                    proposal->noVotes++;
                    break;
                case VOTE_ABSTAIN:
                    proposal->abstainVotes++;
                    break;
            }
        }
    }
}

// Check if voter is registered
bool isVoterRegistered(const char* userId) {
    for (int i = 0; i < contractState.totalRegisteredVoters; i++) {
        if (contractState.voters[i].isRegistered && 
            compareStrings(contractState.voters[i].userId, userId)) {
            return true;
        }
    }
    return false;
}

// Check if voter has already voted on a proposal
bool hasVoterVoted(unsigned int proposalId, const char* userId) {
    for (int i = 0; i < contractState.totalVotes; i++) {
        Vote* vote = &contractState.votes[i];
        if (vote->isValid && 
            vote->proposalId == proposalId && 
            compareStrings(vote->userId, userId)) {
            return true;
        }
    }
    return false;
}

// Check if proposal ID is valid
bool isValidProposal(unsigned int proposalId) {
    return (proposalId > 0 && proposalId <= contractState.totalProposals);
}

// Check if proposal is active
bool isProposalActive(unsigned int proposalId) {
    if (!isValidProposal(proposalId)) return false;
    
    Proposal* proposal = &contractState.proposals[proposalId - 1];
    unsigned long long currentTime = getCurrentTime();
    
    return (proposal->isActive && 
            proposal->status == ACTIVE &&
            currentTime >= proposal->startTime &&
            currentTime <= proposal->endTime);
}

// Get current time (placeholder - should be replaced with Qubic tick)
unsigned long long getCurrentTime() {
    // In a real Qubic smart contract, this would return the current tick
    return 1000000; // Placeholder value
}

// String comparison utility
bool compareStrings(const char* str1, const char* str2) {
    while (*str1 && *str2) {
        if (*str1 != *str2) return false;
        str1++;
        str2++;
    }
    return (*str1 == *str2);
}

// String copy utility
void copyString(char* dest, const char* src, unsigned int maxLength) {
    unsigned int i = 0;
    while (i < maxLength - 1 && src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}

// Get proposal by ID
Proposal getProposal(unsigned int proposalId) {
    if (isValidProposal(proposalId)) {
        return contractState.proposals[proposalId - 1];
    }
    // Return empty proposal if invalid
    Proposal empty = {0};
    return empty;
}

// Get vote by index
Vote getVote(unsigned int voteIndex) {
    if (voteIndex < contractState.totalVotes) {
        return contractState.votes[voteIndex];
    }
    // Return empty vote if invalid
    Vote empty = {0};
    return empty;
}

// Get proposal results
unsigned int getProposalResults(unsigned int proposalId, unsigned int* yesCount, unsigned int* noCount, unsigned int* abstainCount) {
    if (!isValidProposal(proposalId)) {
        *yesCount = 0;
        *noCount = 0;
        *abstainCount = 0;
        return 0;
    }
    
    Proposal* proposal = &contractState.proposals[proposalId - 1];
    *yesCount = proposal->yesVotes;
    *noCount = proposal->noVotes;
    *abstainCount = proposal->abstainVotes;
    
    return proposal->yesVotes + proposal->noVotes + proposal->abstainVotes;
}

// Close a proposal
bool closeProposal(unsigned int proposalId) {
    if (!isValidProposal(proposalId)) {
        return false;
    }
    
    Proposal* proposal = &contractState.proposals[proposalId - 1];
    proposal->status = CLOSED;
    proposal->isActive = false;
    
    return true;
}

// Get total vote count for a proposal
unsigned int getVoteCount(unsigned int proposalId) {
    if (!isValidProposal(proposalId)) {
        return 0;
    }
    
    Proposal* proposal = &contractState.proposals[proposalId - 1];
    return proposal->yesVotes + proposal->noVotes + proposal->abstainVotes;
}

// Simple main function for testing
int main() {
    // Initialize Qubic context
    initQubicContext();
    
    // Initialize the contract
    initializeContract();
    
    // Test creating a proposal
    unsigned int proposalId = createProposal(
        "Test Proposal", 
        "This is a test proposal for the voting system",
        86400 // 1 day duration
    );
    
    // Test registering voters
    registerVoter("alice");
    registerVoter("bob");
    
    // Test voting
    castVote(proposalId, "alice", VOTE_YES, "I support this proposal");
    castVote(proposalId, "bob", VOTE_NO, "I disagree with this");
    
    // Get results
    unsigned int yesCount, noCount, abstainCount;
    unsigned int totalVotes = getProposalResults(proposalId, &yesCount, &noCount, &abstainCount);
    
    return 0; // Success
}