#pragma once

#include "qubic.h"

// Contract constants
#define MAX_VOTES 1000
#define MAX_USER_ID_LENGTH 32
#define MAX_COMMENT_LENGTH 256
#define MAX_PROPOSALS 10

// Vote choice enumeration
enum VoteChoice : unsigned char {
    VOTE_YES = 1,
    VOTE_NO = 2,
    VOTE_ABSTAIN = 3
};

// Vote status enumeration
enum VoteStatus : unsigned char {
    ACTIVE = 1,
    CLOSED = 2,
    PENDING = 3
};

// Proposal structure
struct Proposal {
    unsigned int id;
    char title[64];
    char description[256];
    unsigned long long startTime;
    unsigned long long endTime;
    unsigned int yesVotes;
    unsigned int noVotes;
    unsigned int abstainVotes;
    VoteStatus status;
    m256i creator;
    bool isActive;
};

// Vote structure
struct Vote {
    unsigned int proposalId;
    m256i voterAddress;
    char userId[MAX_USER_ID_LENGTH];
    VoteChoice choice;
    char comment[MAX_COMMENT_LENGTH];
    unsigned long long timestamp;
    unsigned int voteWeight;
    bool isValid;
};

// Voter registration structure
struct Voter {
    m256i address;
    char userId[MAX_USER_ID_LENGTH];
    bool isRegistered;
    unsigned int reputation;
    unsigned long long registrationTime;
};

// Contract state
struct CONTRACT_STATE {
    unsigned int totalVotes;
    unsigned int totalProposals;
    unsigned int totalRegisteredVoters;
    unsigned long long contractCreationTime;
    m256i contractOwner;
    bool isActive;
    
    // Storage arrays
    Vote votes[MAX_VOTES];
    Proposal proposals[MAX_PROPOSALS];
    Voter voters[MAX_VOTES]; // Reuse MAX_VOTES for voters limit
};

// Function declarations (no implementations in header)
void initializeContract();
unsigned int createProposal(const char* title, const char* description, unsigned long long duration);
bool registerVoter(const char* userId);
bool castVote(unsigned int proposalId, const char* userId, VoteChoice choice, const char* comment);
unsigned int getVoteCount(unsigned int proposalId);
bool closeProposal(unsigned int proposalId);
bool isVoterRegistered(const char* userId);
bool hasVoterVoted(unsigned int proposalId, const char* userId);
Proposal getProposal(unsigned int proposalId);
Vote getVote(unsigned int voteIndex);
unsigned int getProposalResults(unsigned int proposalId, unsigned int* yesCount, unsigned int* noCount, unsigned int* abstainCount);

// Utility functions
bool isValidProposal(unsigned int proposalId);
bool isProposalActive(unsigned int proposalId);
void updateProposalVoteCounts(unsigned int proposalId);
unsigned long long getCurrentTime();
bool compareStrings(const char* str1, const char* str2);
void copyString(char* dest, const char* src, unsigned int maxLength);

// External contract state declaration
extern CONTRACT_STATE contractState;
