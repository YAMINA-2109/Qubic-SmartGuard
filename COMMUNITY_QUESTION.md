# Message for Qubic Community (Discord/Telegram)

## Post This Message:

---

**Subject: Smart Contract Query Parameters for RPC Integration**

Hi Qubic community! 👋

I'm building a blockchain monitoring tool using the official Qubic RPC API (`https://rpc.qubic.org`) and have successfully implemented:

- ✅ Network status monitoring
- ✅ Tick information
- ✅ Transaction data retrieval
- ✅ Balance queries

Now I need help with smart contract queries using `POST /v1/querySmartContract`. I can see the endpoint is available, but I need the specific contract parameters:

### 🔥 For Burn Statistics:

```
❓ What is the contractIndex for querying burn data?
❓ What inputType should I use to get total burned QUBIC?
❓ What does the responseData format look like?
```

### 🗳️ For Governance/Voting:

```
❓ What is the contractIndex for governance/voting?
❓ What inputType gets active proposals?
❓ What inputType gets vote counts?
❓ How is the response data structured?
```

### 📋 Example of what I need:

```json
// Burns query example
{
  "contractIndex": ?,    // What number?
  "inputType": ?,        // What number for burn stats?
  "inputSize": ?,
  "requestData": ""
}

// Governance query example
{
  "contractIndex": ?,    // What number?
  "inputType": ?,        // What number for proposals?
  "inputSize": ?,
  "requestData": ""
}
```

### 🤔 Alternative Question:

Is there a **contract registry** or **contract documentation** that lists:

- Available smart contracts and their indices
- Function types (inputType) for each contract
- Data encoding/decoding formats

Or if there's a simpler way:

- Is there a public burn address I can query instead?
- Is there a governance contract address?

**Any documentation, examples, or guidance would be greatly appreciated!** 🙏

Currently using: `https://qubic.github.io/integration/Partners/swagger/` for API docs, but it doesn't include contract-specific details.

Thanks for your help! 🚀

---

## Alternative Shorter Version:

---

Hey Qubic devs! Quick question about RPC smart contract queries:

What are the contractIndex and inputType values for:

1. 🔥 Querying burn statistics?
2. 🗳️ Querying governance/voting data?

Using: `POST /v1/querySmartContract` at https://rpc.qubic.org

Any docs or examples? Thanks! 🙏

---

## Where to Post:

1. **Qubic Discord** - #developer-chat or #api-integration channel
2. **Qubic Telegram** - Developer group
3. **Qubic GitHub** - Open an issue in the docs repository
4. **Qubic Reddit** - r/Qubic if exists
5. **Qubic Forum** - If they have one

---

## What to Expect:

Community members or devs should respond with something like:

```
Burns: contractIndex = 5, inputType = 1 for getTotalBurned
Governance: contractIndex = 10, inputType = 2 for getProposals
```

Or point you to contract documentation.

Once you get this info, implementation will take ~2 hours! 🚀
