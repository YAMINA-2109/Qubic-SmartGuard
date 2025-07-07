using namespace QPI;

/**
 * Custom Smart Contract: HM25Plus
 * Features:
 * - Echo: Returns the full invocation reward
 * - Burn: Burns the reward
 * - Bonus: Returns half the reward
 * - GetAllStats: Returns all call counters
 */

struct HM25Plus : public ContractBase
{
public:
    struct Echo_input {};
    struct Echo_output {};

    struct Burn_input {};
    struct Burn_output {};

    struct Bonus_input {};
    struct Bonus_output {};

    struct GetAllStats_input {};
    struct GetAllStats_output
    {
        uint64 numberOfEchoCalls;
        uint64 numberOfBurnCalls;
        uint64 numberOfBonusCalls;
    };

private:
    struct State
    {
        uint64 numberOfEchoCalls;
        uint64 numberOfBurnCalls;
        uint64 numberOfBonusCalls;
    } state;

    HM25Plus()
    {
        state.numberOfEchoCalls = 0;
        state.numberOfBurnCalls = 0;
        state.numberOfBonusCalls = 0;
    }

    /**
     * Echo: Return full reward to invocator
     */
    QPI_PROCEDURE(Echo)
    {
        state.numberOfEchoCalls++;
        if (qpi.invocationReward() > 0)
        {
            qpi.transfer(qpi.invocator(), qpi.invocationReward());
        }
    }

    /**
     * Burn: Remove reward from circulation
     */
    QPI_PROCEDURE(Burn)
    {
        state.numberOfBurnCalls++;
        if (qpi.invocationReward() > 0)
        {
            qpi.burn(qpi.invocationReward());
        }
    }

    /**
     * Bonus: Return half reward to invocator
     */
    QPI_PROCEDURE(Bonus)
    {
        state.numberOfBonusCalls++;
        uint64 reward = qpi.invocationReward();
        if (reward > 1)
        {
            qpi.transfer(qpi.invocator(), reward / 2);
            qpi.burn(reward - (reward / 2));
        }
    }

    /**
     * GetAllStats: Return all call counters
     */
    QPI_FUNCTION(GetAllStats)
    {
        GetAllStats_output output;
        output.numberOfEchoCalls = state.numberOfEchoCalls;
        output.numberOfBurnCalls = state.numberOfBurnCalls;
        output.numberOfBonusCalls = state.numberOfBonusCalls;
        return output;
    }

    REGISTER_USER_FUNCTIONS_AND_PROCEDURES
    {
        REGISTER_USER_PROCEDURE(Echo, 1);
        REGISTER_USER_PROCEDURE(Burn, 2);
        REGISTER_USER_PROCEDURE(Bonus, 3);
        REGISTER_USER_FUNCTION(GetAllStats, 1);
    }

    INITIALIZE
    {
        state.numberOfEchoCalls = 0;
        state.numberOfBurnCalls = 0;
        state.numberOfBonusCalls = 0;
    }
};
