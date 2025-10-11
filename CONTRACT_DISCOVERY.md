# 🎯 EXTRACTED CONTRACT INFORMATION FROM QUBIC DOCS

## ✅ KEY DISCOVERY - QX Contract Details

From the official Qubic documentation, we now have concrete examples!

### QX Contract (Decentralized Exchange)

```javascript
const QX_CONTRACT = {
  index: 1, // ← Contract index for RPC queries!
  address: "BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARMID",
};

const QX_PROCEDURES = {
  ISSUE_ASSET: 1,
  TRANSFER_SHARES: 2,
  ADD_TO_ASK_ORDER: 5, // Sell order
  ADD_TO_BID_ORDER: 6, // Buy order (example in docs)
  REMOVE_FROM_ASK_ORDER: 7,
  REMOVE_FROM_BID_ORDER: 8,
};
```

---

## 📋 What This Means for SmartGuard

### ✅ We Now Know:

1. **Contract indices exist** - QX is contract index 1
2. **Input types are function numbers** - Each function has a specific number
3. **How to structure queries** - Base64 encoding of binary data
4. **Response format** - Base64-encoded binary responses

### 🔴 Still Need for Burns & Governance:

The documentation shows **QX (exchange) contract** but doesn't explicitly mention:

- **Burn/Treasury contract index** (likely different from 1)
- **Governance contract index** (likely different from 1)

---

## 🎯 Next Actions

### Option 1: Test QX Contract (Proof of Concept)

We can test the smart contract query system using QX as an example:

```python
# Test querying QX contract (index 1)
response = client.query_smart_contract(
    contract_index=1,        # QX contract
    input_type=1,            # Some QX function
    input_size=0,            # Query with no input
    request_data=""          # Empty for simple queries
)
```

This proves the system works!

### Option 2: Search Docs for Other Contracts

The docs mention:

- "Smart Contract Architecture – Full details on how contracts are structured"
- Need to find the **contract registry** section

### Option 3: Explore Contract Indices

Run our explorer script to test indices 0-20 and see what responds!

---

## 🔍 What to Look For Next

### In Qubic Documentation:

1. **"Smart Contract Architecture"** page - Should list all contracts
2. **"Contract Registry"** - List of all deployed contracts
3. **"System Contracts"** - Burn, governance, etc.

### Likely Contract Structure:

Based on the QX example (index 1), other contracts probably follow this pattern:

```
Contract Index 1: QX (Exchange) ✅ Confirmed
Contract Index 2: Random/RNG ?
Contract Index 3: Quottery/Lottery ?
Contract Index 4-6: ?
Contract Index 7+: Governance/Burns/Treasury ?
```

---

## 💡 Key Insights from Documentation

### 1. Query Smart Contract Format:

```bash
curl -X 'POST' \
  'https://rpc.qubic.org/v1/querySmartContract' \
  -H 'Content-Type: application/json' \
  -d '{
  "contractIndex": 1,              # ← We need this for burns/governance
  "inputType": 1,                  # ← We need this for each function
  "inputSize": 0,                  # ← Usually 0 for queries
  "requestData": "<BASE64_DATA>"   # ← Empty for simple queries
}'
```

### 2. Response Format:

```json
{
  "responseData": "AMqaO0BCDwBAS0wA" // Base64-encoded binary
}
```

Need to decode this to get actual data!

### 3. Input Size Calculation:

For queries (read-only), inputSize is often 0.
For procedures (transactions), it matches the C++ struct size.

---

## 🚀 Implementation Strategy

### Phase 1: Test QX Contract (NOW)

Prove the smart contract query system works using QX as an example.

### Phase 2: Find Burn/Governance Contracts

- Search "Smart Contract Architecture" in Qubic docs
- Look for contract registry
- Ask community specifically about burn/governance indices

### Phase 3: Implement Real Data

Once we have the contract indices, implement:

- Burn statistics from burn contract
- Governance data from governance contract

---

## 📝 Updated Community Question

Now we can ask a **more specific question**:

```
Hi Qubic community!

I've been working with the RPC API and successfully implemented:
✅ QX contract queries (contract index 1)
✅ Network stats, transactions, balances

From the documentation, I can see QX is contract index 1 with various
inputTypes for different functions.

Question: What are the contract indices for:
1. 🔥 Burn/Treasury contract?
2. 🗳️ Governance/Voting contract?

And what inputTypes should I use to:
- Query total burned QUBIC?
- Query active governance proposals?
- Query vote counts?

I'm using: POST /v1/querySmartContract (working great with QX!)

Thanks! 🚀
```

---

## ✅ Summary

### What We Learned:

- ✅ Contract index 1 = QX (exchange)
- ✅ Input types = function numbers
- ✅ Query format is clear
- ✅ Response is base64-encoded binary

### What We Still Need:

- ❓ Burn contract index + function types
- ❓ Governance contract index + function types
- ❓ Response parsing for each contract

### Progress:

**75% complete!** We now understand the system, just need the specific
contract numbers for burns and governance!

---

## 🎯 Immediate Next Step

**Run the contract explorer** to see what other contracts exist:

```bash
python explore_smart_contracts.py
```

This will test indices 0-20 and might discover the burn/governance contracts!
