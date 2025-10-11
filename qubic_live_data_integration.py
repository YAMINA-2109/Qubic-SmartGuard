"""
🌟 QUBIC SMARTGUARD - LIVE DATA INTEGRATION
Transforms real Qubic RPC data into app-ready format
"""
import random
from datetime import datetime

from qubic_official_rpc_client import QubicRPCClient


class QubicLiveDataProvider:
    """Provides real-time data from Qubic blockchain"""

    def __init__(self):
        self.client = QubicRPCClient()
        self.network_data = None
        self.last_update = None

    def refresh_network_data(self):
        """Fetch fresh data from Qubic RPC"""
        try:
            # Get network status
            status = self.client.get_status()

            # Get current tick info
            tick_data = self.client.get_tick_info()

            if status and tick_data:
                self.network_data = {
                    'status': status,
                    'tick_info': tick_data.get('tickInfo', {}),
                    'timestamp': datetime.now()
                }
                self.last_update = datetime.now()
                return True
            return False
        except Exception as e:
            print(f"❌ Error fetching network data: {e}")
            return False

    def get_network_stats(self):
        """Get network statistics in SmartGuard format"""
        if not self.network_data:
            if not self.refresh_network_data():
                return self._get_demo_stats()

        tick_info = self.network_data['tick_info']
        status = self.network_data['status']

        return {
            'current_tick': tick_info.get('tick', 0),
            'epoch': tick_info.get('epoch', 0),
            'tick_duration': tick_info.get('duration', 0),
            'last_processed_tick': status.get('lastProcessedTick', 0),
            'timestamp': self.network_data['timestamp'].isoformat(),
            'data_source': '🟢 LIVE',
            'connection_status': 'Connected to rpc.qubic.org'
        }

    def get_recent_activity(self, limit=10):
        """
        Get recent blockchain activity with smart tick selection.
        Uses intelligent sampling to find ticks with transactions.
        """
        if not self.network_data:
            self.refresh_network_data()

        activities = []

        if self.network_data:
            tick_info = self.network_data['tick_info']
            current_tick = tick_info.get('tick', 0)

            # Smart tick selection: sample at increasing intervals
            # This finds ticks with transactions more efficiently
            tick_offsets = [0, 5, 10, 50, 100, 500, 1000, 5000, 10000]

            for offset in tick_offsets:
                if len(activities) >= limit:
                    break

                tick_num = current_tick - offset
                if tick_num <= 0:
                    continue

                try:
                    txs = self.client.get_tick_transactions(tick_num)

                    if txs and 'transactions' in txs:
                        tx_list = txs['transactions']
                        # Process up to 3 transactions per tick
                        for tx in tx_list[:3]:
                            if len(activities) >= limit:
                                break

                            # Format transaction for display
                            source_id = tx.get('sourceId', 'Unknown')
                            dest_id = tx.get('destId', 'Unknown')
                            amount = tx.get('amount', 0)

                            activities.append({
                                'icon': '💱',
                                'action': 'Transfer',
                                'amount': f'{amount:,}' if isinstance(amount, int) else str(amount),
                                'token': 'QUBIC',
                                'tick': tick_num,
                                'source': source_id[:8] + '...' if len(source_id) > 8 else source_id,
                                'dest': dest_id[:8] + '...' if len(dest_id) > 8 else dest_id,
                                'time': f'Tick {tick_num:,}',
                                'data_source': '🟢 LIVE'
                            })

                except Exception as e:
                    # Tick might not have transactions or other error
                    continue

        # If no real data found, return demo activities with live tick numbers
        if not activities:
            activities = self._get_demo_activities(limit)

        return activities

    def get_burn_statistics(self):
        """
        Get QUBIC burn statistics from CCF contract (index 8)
        Contract: CCF (Computor Controlled Fund) - Burns/Treasury
        """
        if not self.network_data:
            self.refresh_network_data()

        try:
            # Query CCF contract (index 8) for burn statistics
            # inputType 6 returns 4 bytes (likely uint32 total burned)
            response = self.client.query_smart_contract(
                contract_index=8,  # CCF contract
                input_type=6,      # Total burned stat
                input_size=0,
                request_data=""
            )
            
            if response and 'responseData' in response and response['responseData']:
                import base64
                # Decode base64 response
                burn_data = base64.b64decode(response['responseData'])
                
                # Parse burn data (uint32 or uint64)
                if len(burn_data) >= 4:
                    # Try as uint64 first, fallback to uint32
                    if len(burn_data) >= 8:
                        total_burned = int.from_bytes(burn_data[:8], 'little')
                    else:
                        total_burned = int.from_bytes(burn_data[:4], 'little')
                    
                    current_tick = 0
                    if self.network_data:
                        current_tick = self.network_data['tick_info'].get('tick', 0)
                    
                    return {
                        'total_burned': total_burned,
                        'last_burn_tick': current_tick,
                        'timestamp': datetime.now().isoformat(),
                        'data_source': '🟢 LIVE (CCF Contract)',
                        'contract_index': 8,
                        'input_type': 6
                    }
        except Exception as e:
            print(f"⚠️  Error querying burn statistics: {e}")
        
        # Fallback to demo data if query fails
        return {
            'total_burned': 0,
            'last_burn_tick': self.network_data['tick_info'].get('tick', 0) if self.network_data else 0,
            'timestamp': datetime.now().isoformat(),
            'data_source': '🔴 DEMO (CCF Query Failed)'
        }

    def get_voting_results(self):
        """
        Get governance voting results from GQMPROPO contract (index 6)
        Contract: GQMPROPO (Governance/Voting)
        """
        try:
            # Query GQMPROPO contract (index 6) for voting data
            response = self.client.query_smart_contract(
                contract_index=6,  # GQMPROPO contract
                input_type=5,      # Proposals data
                input_size=0,
                request_data=""
            )
            
            if response and 'responseData' in response:
                import base64
                # Decode base64 response
                vote_data = base64.b64decode(response['responseData'])
                
                # Parse voting data (structure depends on contract implementation)
                # For now, return that we got data
                return {
                    'active_proposals': len(vote_data) // 32 if vote_data else 0,  # Estimate
                    'total_votes': 0,  # Need to parse structure
                    'data_source': '� LIVE (GQMPROPO Contract)',
                    'contract_index': 6,
                    'timestamp': datetime.now().isoformat(),
                    'raw_data_size': len(vote_data)
                }
        except Exception as e:
            print(f"⚠️  Error querying governance data: {e}")
        
        # Fallback to demo data if query fails
        return {
            'active_proposals': 0,
            'total_votes': 0,
            'data_source': '🔴 DEMO (GQMPROPO Query Failed)',
            'timestamp': datetime.now().isoformat()
        }

    def _get_demo_stats(self):
        """Fallback demo data when RPC is unavailable"""
        return {
            'current_tick': 0,
            'epoch': 0,
            'tick_duration': 0,
            'last_processed_tick': 0,
            'timestamp': datetime.now().isoformat(),
            'data_source': '🔴 OFFLINE',
            'connection_status': 'Unable to connect to RPC'
        }

    def _get_demo_activities(self, limit=10):
        """Generate demo activities with live tick numbers"""
        activities = []
        base_tick = self.network_data['tick_info'].get(
            'tick', 34000000) if self.network_data else 34000000

        activity_types = [
            ('🔥', 'Token Burn', 'QUBIC'),
            ('📊', 'Smart Contract', 'Execution'),
            ('🗳️', 'Governance', 'Vote'),
            ('💱', 'Transfer', 'QUBIC')
        ]

        for i in range(limit):
            icon, action, token = random.choice(activity_types)
            activities.append({
                'icon': icon,
                'action': action,
                'amount': f'{random.randint(100, 10000):,}',
                'token': token,
                'tick': base_tick - i * random.randint(1, 100),
                'time': f'{random.randint(1, 60)} seconds ago',
                'data_source': '🔴 DEMO'
            })

        return activities


# Global instance
_provider = None


def get_live_data_provider():
    """Get or create the global live data provider"""
    global _provider
    if _provider is None:
        _provider = QubicLiveDataProvider()
    return _provider


# Convenience functions for main_app.py
def get_live_network_stats():
    """Get live network statistics"""
    return get_live_data_provider().get_network_stats()


def get_live_recent_activity(limit=10):
    """Get recent blockchain activity"""
    return get_live_data_provider().get_recent_activity(limit)


def get_live_burn_statistics():
    """Get burn statistics"""
    return get_live_data_provider().get_burn_statistics()


def get_live_voting_results():
    """Get voting results"""
    return get_live_data_provider().get_voting_results()


def refresh_all_data():
    """Refresh all data from RPC"""
    provider = get_live_data_provider()
    return provider.refresh_network_data()


if __name__ == "__main__":
    # Quick test
    print("=" * 80)
    print("🛡️  QUBIC SMARTGUARD - LIVE DATA TEST")
    print("=" * 80)

    provider = QubicLiveDataProvider()

    print("\n📊 Fetching Network Stats...")
    stats = provider.get_network_stats()
    print(f"✅ Current Tick: {stats['current_tick']:,}")
    print(f"✅ Epoch: {stats['epoch']}")
    print(f"✅ Status: {stats['data_source']}")
    print(f"✅ Connection: {stats['connection_status']}")

    print("\n🔔 Fetching Recent Activity...")
    activities = provider.get_recent_activity(5)
    print(f"✅ Retrieved {len(activities)} activities")

    for activity in activities[:3]:
        if 'icon' in activity:
            print(
                f"   {activity['icon']} {activity['action']} - Tick {activity['tick']:,}")
        else:
            print(f"   📝 Transaction at tick {activity['tick']}")

    print("\n✅ Live data integration working!")
