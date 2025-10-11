# 🎉 CONTRACT FUNCTIONS DISCOVERED!

## ✅ CCF Contract (Index 8) - Burns/Treasury

### Working Functions:

| inputType | Response Size    | Likely Purpose                    |
| --------- | ---------------- | --------------------------------- |
| 0         | Empty            | Status/ping                       |
| 1         | 130 bytes        | **Contract info/stats**           |
| 2         | 344 bytes        | **Detailed data**                 |
| 3         | 24 bytes         | Counter/stat                      |
| 4         | 56 bytes         | Configuration                     |
| 5         | **38,912 bytes** | **Large dataset (burn records?)** |
| 6         | 4 bytes          | **Simple stat (total burned?)**   |
| 7-9       | Empty            | Not used                          |

### Most Promising for Burn Stats:

- **inputType 6**: 4 bytes (could be uint32 total burned)
- **inputType 5**: 38KB of data (detailed burn records)
- **inputType 2**: 344 bytes (summary data)

---

## ✅ GQMPROPO Contract (Index 6) - Governance/Voting

### Working Functions:

| inputType | Response Size   | Likely Purpose                                       |
| --------- | --------------- | ---------------------------------------------------- |
| 0         | Empty           | Status/ping                                          |
| 1         | 130 bytes       | Contract info/stats                                  |
| 2         | 368 bytes       | Detailed data                                        |
| 3         | 24 bytes        | Counter/stat                                         |
| 4         | 56 bytes        | Configuration                                        |
| 5         | **6,144 bytes** | **Proposals data (starts with 0x07 = 7 proposals?)** |
| 6-9       | Empty           | Not used                                             |

### Most Promising for Governance:

- **inputType 5**: 6KB starting with `07 00 00 00...` (7 proposals?)
- **inputType 2**: 368 bytes (summary data)
- **inputType 3**: 24 bytes (vote count?)

---

## 🎯 Interpretation

### CCF inputType 6 (4 bytes):

```
Hex: 40420f00
As uint32 (little-endian): 1,000,000 (0x0F4240)
Could be: Total burned = 1,000,000 QUBIC
```

### GQMPROPO inputType 5 (first 8 bytes):

```
Hex: 0700000000000000
As uint64: 7
Likely: 7 active proposals
```

---

## 💡 Recommended Implementation

### For Burns (CCF Contract 8):

```python
# inputType 6: Likely total burned (uint32 or uint64)
response = query_smart_contract(8, 6, 0, "")
total_burned = int.from_bytes(data[:4], 'little')  # or [:8] if uint64
```

### For Governance (GQMPROPO Contract 6):

```python
# inputType 5: First uint64 is proposal count
response = query_smart_contract(6, 5, 0, "")
proposal_count = int.from_bytes(data[:8], 'little')
```

---

## 🚀 Next Action

Update `qubic_live_data_integration.py` with:

- CCF inputType 6 for burn statistics
- GQMPROPO inputType 5 for proposal count
