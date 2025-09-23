def load_domain_categories():
    """Load our email domain security categories"""
    

    high_risk = {
        "hacknotice.com",
        "cyberdefense.com", 
        "cyberhillpartners.com",
        "cyberpaperpushers-it.com"
    }
    
    medium_risk = {
        "alteryx.com",
        "druva.com",
        "dataappendservice.com", 
        "datadigitalcenter.com",
        "dataitlab.com",
        "datasolutionprovide.com"
    }
    
    marketing_domains = {
        "e.alteryx.com",
        "em.proofpoint.com", 
        "email.box.com",
        "email.emeraldclub.com",
        "email.empower.com"
    }
    
    return high_risk, medium_risk, marketing_domains

def calculate_risk_score(domain, high_risk, medium_risk):
    """Calculate a numeric risk score for a domain"""
    base_score = 0
    
    # Direct matches
    if domain in high_risk:
        base_score += 100
    elif domain in medium_risk:
        base_score += 50
    
    # Pattern analysis
    risk_keywords = ["cyber", "hack", "data", "append", "blast"]
    for keyword in risk_keywords:
        if keyword in domain:
            base_score += 10
    
    # Subdomain analysis
    if domain.startswith("e.") or domain.startswith("email."):
        base_score += 25  # Marketing subdomains
    
    return base_score

def determine_action(risk_score, user_security_level):
    """Decide what action to take based on risk score and user preference"""
    
    if user_security_level == "strict":
        if risk_score >= 25:
            return "BLOCK"
        else:
            return "ALLOW"
    elif user_security_level == "moderate":
        if risk_score >= 50:
            return "BLOCK"
        elif risk_score >= 25:
            return "QUARANTINE"
        else:
            return "ALLOW"
    else:  # relaxed
        if risk_score >= 75:
            return "BLOCK"
        elif risk_score >= 50:
            return "QUARANTINE"
        else:
            return "ALLOW"

def process_email_batch(email_domains, high_risk, medium_risk, security_level):
    """Process multiple email domains and return results"""
    
    results = {
        "blocked": set(),
        "quarantined": set(), 
        "allowed": set()
    }
    
    for domain in email_domains:
        # Calculate risk for this domain
        risk = calculate_risk_score(domain, high_risk, medium_risk)
        
        # Determine action
        action = determine_action(risk, security_level)
        
        # Store result
        if action == "BLOCK":
            results["blocked"].add(domain)
        elif action == "QUARANTINE":
            results["quarantined"].add(domain)
        else:
            results["allowed"].add(domain)
    
    return results

def generate_security_report(results, high_risk, medium_risk):
    """Generate a comprehensive security report"""
    
    print("=" * 50)
    print("EMAIL SECURITY ANALYSIS REPORT")
    print("=" * 50)
    
    # Basic statistics
    total_processed = len(results["blocked"]) + len(results["quarantined"]) + len(results["allowed"])
    blocked_count = len(results["blocked"])
    quarantined_count = len(results["quarantined"])
    allowed_count = len(results["allowed"])
    
    print(f"\n📊 PROCESSING SUMMARY:")
    print(f"   Total emails processed: {total_processed}")
    print(f"   🚫 Blocked: {blocked_count} ({blocked_count/total_processed*100:.1f}%)")
    print(f"   ⚠️  Quarantined: {quarantined_count} ({quarantined_count/total_processed*100:.1f}%)")
    print(f"   ✅ Allowed: {allowed_count} ({allowed_count/total_processed*100:.1f}%)")
    
    # Set analysis
    print(f"\n🔍 THREAT ANALYSIS:")
    
    # Which known threats were caught?
    caught_high_risk = results["blocked"] & high_risk
    caught_medium_risk = results["blocked"] & medium_risk
    
    print(f"   Known high-risk domains blocked: {len(caught_high_risk)}")
    if caught_high_risk:
        print(f"      {sorted(caught_high_risk)}")
    
    print(f"   Known medium-risk domains blocked: {len(caught_medium_risk)}")
    if caught_medium_risk:
        print(f"      {sorted(caught_medium_risk)}")
    
    # Unknown threats (blocked domains not in our lists)
    unknown_blocks = results["blocked"] - (high_risk | medium_risk)
    if unknown_blocks:
        print(f"   🆕 New potential threats discovered: {len(unknown_blocks)}")
        print(f"      {sorted(unknown_blocks)}")

def main():
    """Orchestrate the complete email security analysis"""
    
    print("🔐 Email Security Manager Starting...")
    
    # Step 1: Load our threat intelligence
    high_risk, medium_risk, marketing = load_domain_categories()
    
    # Step 2: Simulate incoming email domains
    incoming_emails = {
        "hacknotice.com",           # Known high risk
        "dataappendservice.com",    # Known medium risk  
        "google.com",               # Clean
        "suspicious-new-domain.ru", # Unknown potential threat
        "email.box.com",            # Marketing
        "etsu.edu",                 # Clean educational
        "cyber-threat-new.net",     # Unknown potential threat
        "druva.com"                 # Known medium risk
    }
    
    print(f"📧 Processing {len(incoming_emails)} incoming emails...")
    
    # Step 3: Get user security preference
    print("\nSecurity Levels:")
    print("  strict   - Block anything suspicious")
    print("  moderate - Balance security and convenience") 
    print("  relaxed  - Only block obvious threats")
    
    security_level = input("Choose security level (strict/moderate/relaxed): ").strip().lower()
    if security_level not in ["strict", "moderate", "relaxed"]:
        security_level = "moderate"
        print("Invalid choice, using 'moderate'")
    
    # Step 4: Process the email batch
    results = process_email_batch(incoming_emails, high_risk, medium_risk, security_level)
    
    # Step 5: Generate comprehensive report
    generate_security_report(results, high_risk, medium_risk)
    
    print(f"\n🎯 Security analysis complete using '{security_level}' settings.")

if __name__ == "__main__":
    main()