import time
import threading
from modules.threat_intelligence import fetch_threat_intel
from modules.risk_scoring import calculate_risk_score
from modules.compliance_checker import check_compliance
from modules.monitoring import monitor_third_parties
from modules.dashboard import launch_dashboard

def run_threat_intel():
    """Fetches and processes real-time threat intelligence."""
    while True:
        threats = fetch_threat_intel()
        print(f"[Threat Intelligence] {len(threats)} new threats analyzed.")
        time.sleep(3600)  # Run hourly

def run_risk_scoring():
    """Calculates risk scores dynamically based on threat intelligence and vendor data."""
    while True:
        risk_data = calculate_risk_score()
        print(f"[Risk Scoring] Updated risk scores for vendors.")
        time.sleep(86400)  # Run daily

def run_compliance_check():
    """Checks third-party vendors against regulatory compliance frameworks."""
    while True:
        compliance_status = check_compliance()
        print(f"[Compliance Check] Compliance status updated.")
        time.sleep(86400)  # Run daily

def run_monitoring():
    """Continuously monitors third-party behavior for anomalies."""
    while True:
        alerts = monitor_third_parties()
        print(f"[Monitoring] {len(alerts)} security alerts generated.")
        time.sleep(1800)  # Run every 30 minutes

def main():
    """Main function to start all core components."""
    print("Starting RiskNexus - Automated Third-Party Risk Assessment...")
    
    # Launching individual components as threads
    threading.Thread(target=run_threat_intel, daemon=True).start()
    threading.Thread(target=run_risk_scoring, daemon=True).start()
    threading.Thread(target=run_compliance_check, daemon=True).start()
    threading.Thread(target=run_monitoring, daemon=True).start()
    
    # Start the dashboard interface
    launch_dashboard()
    
if __name__ == "__main__":
    main()
