"""
Test improved transaction fetching with smart tick selection
"""
from qubic_live_data_integration import get_live_recent_activity


def main():
    print("=" * 80)
    print("🧪 TESTING IMPROVED TRANSACTION FETCHING")
    print("=" * 80)
    print()
    print("Old method: Check ticks sequentially (0, 1, 2, 3...)")
    print("New method: Check ticks at smart intervals (0, 5, 10, 50, 100...)")
    print()
    print("=" * 80)
    print()

    print("📊 Fetching recent activity with smart sampling...")
    print()

    activities = get_live_recent_activity(limit=10)

    print(f"✅ Retrieved {len(activities)} activities")
    print()
    print("=" * 80)
    print("📋 ACTIVITY FEED")
    print("=" * 80)
    print()

    for i, activity in enumerate(activities, 1):
        icon = activity.get('icon', '📝')
        action = activity.get('action', 'Activity')
        tick = activity.get('tick', 0)
        amount = activity.get('amount', 'N/A')
        source = activity.get('source', 'N/A')
        dest = activity.get('dest', 'N/A')
        data_source = activity.get('data_source', '🔴 DEMO')

        print(f"{i}. {icon} {action}")
        print(f"   Tick: {tick:,}")
        print(f"   Amount: {amount}")
        print(f"   From: {source}")
        print(f"   To: {dest}")
        print(f"   Source: {data_source}")
        print()

    # Count real vs demo
    live_count = sum(1 for a in activities if '🟢' in str(
        a.get('data_source', '')))
    demo_count = len(activities) - live_count

    print("=" * 80)
    print("📊 RESULTS")
    print("=" * 80)
    print(f"🟢 Live Transactions: {live_count}")
    print(f"🔴 Demo Data: {demo_count}")
    print()

    if live_count > 0:
        print("✅ SUCCESS! Found real blockchain transactions!")
        print("✅ Smart tick selection is working!")
    elif demo_count == len(activities):
        print("⚠️  No real transactions found (using demo data)")
        print("⚠️  This can happen if recent ticks have no transactions")

    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
