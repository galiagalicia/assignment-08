# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Data Backup":125,
    "Cybersecurity": 185,
    "Hardware Maintenance": 250,
}

# TODO 2: Create customer dictionaries
customer1 = {
    "company_name": "ABC Corp",
    "contact_person": "John Smith",
    "email": "jsmith@corp.org",
    "phone": "813-031-0940"
}

customer2 = {
    "company_name": "NVIDIA",
    "contact_person": "Bob Williams",
    "email": "bwilliams@nvidia.org",
    "phone": "813-356-4960"
}

customer3 = {
    "company_name": "Apple",
    "contact_person": "Emma Brown",
    "email": "ebrown@apple.org",
    "phone": "813-076-1407"
}

customer4 = {
    "company_name": "Microsoft",
    "contact_person": "Anna Johnson",
    "email": "ajohnson@microsoft.org",
    "phone": "813-892-0045"
}

# TODO 3: Create a master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)

for cid, info in customers.items():
    print("Customer ID:", cid)
    for key, value in info.items():
        print(key, ":", value)
    print()
    
# TODO 5: Look up specific customers
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)

print("C002 Info:", c002_info)
print("C003 Contact:", c003_contact)
print("C999:", c999_info)

# TODO 6: Update customer information
customers["C001"]["phone"] = "813-497-0101" #update
customers["C002"]["industry"] = "Security" # adds new key value pair

print("\n\nUpdating Customer Information:")
print("-" * 60)

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
project1 = {"name":  "Custome Website", "service": "Web Development", "hours": 150, "budget": 20000}
project2 = {"name": "Date Consulting", "service": "Data Analysis", "hours": 135, "budget":15000}
project3 = {"name": "Incremental Backup", "service": "Data Backup", "hours": 140, "budget": 17500}
project4 = {"name": "Network Security", "service": "Cybersecurity", "hours": 160, "budget": 25000}
project5 = {"name": "Hardware Installation", "service": "Hardware Maintenance", "hours": 170, "budget": 30000}

print("\n\nProject Information:")
print("-" * 60)

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4],
    "C004": [project5]
}

print("\n\nProject Information:")
print("-" * 60)

for cid, plist in projects.items():
    print("Customer:", cid)
    for p in plist:
        print(p)
    print()
    
# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)

for cid, plist in projects.items():
    for p in plist:
        rate = services[p["service"]]
        cost = rate *p["hours"]
        print(p["name"], "-:", cost)
        
# TODO 9: Customer statistics using dictionary methods
print("\n\nCustomer Statistics:")
print("-" * 60)

print("Customer IDs:", list(customers.keys()))

companies = [c["company_name"] for c in customers.values()]
print("Customer Companies:", companies)

print("Total Customers:", len(customers))

# TODO 10: Service usage analysis
service_counts = {} # empty dictionary 

for plist in projects.values():
    for p in plist:
        service = p["service"]
        service_counts[service] = service_counts.get(service, 0) + 1
    
print("\n\nService Usage Analysis:")
print("-" * 60)

print(service_counts)

# TODO 11: Financial aggregations
total_hours = 0 # start at 0 
budgets = [] # empty list 

for plist in projects.values():
    for p in plist:
        total_hours += p["hours"]
        budgets.append(p["budget"])
        
total_budget = sum(budgets)
avg_budget = total_budget / len(budgets)
max_budget = max(budgets)
min_budget = min(budgets)

print("\n\nFinancial Summary:")
print("-" * 60)

print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Max Budget:", max_budget)
print("Min Budget:", min_budget)

# TODO 12: Customer summary report
print("\n\nCustomer Summary Report:")
print("-" * 60)

for cid, data in customers.items():
    plist = projects.get(cid, [])
    customer_hours = sum(p["hours"] for p in plist)
    customer_budgets = sum(p["budget"] for p in plist)
    
    print(data["company_name"])
    print("Projects", len(plist))
    print("Total Hours:", customer_hours)
    print(f"{cid} Total Budget: ${customer_budgets}")
    print()
    
# TODO 13: Create rate adjustments using dictionary comprehension
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
active_customers = {cid: info for cid, info in customers.items() if cid in projects}

print("\n\nActive Customers (with projects):")
print("-" * 60)
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
service_tiers = {
    s: "Premium" if r >= 200 else "Standard" if r >= 100 else "Basic"
    for s, r in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# TODO 17: Customer validation function
def validate_customer(customer_dict):
    required = ["company_name", "contact_person", "email", "phone"]
    for field in required:
        if field not in customer_dict:
            return False
    return True 

print("\n\nCustomer Validation:")
print("-" * 60)

for cid, customer in customers.items():
    print(cid, validate_customer(customer))
    
# TODO 18: Project status tracking with loops and conditionals
status_counts = {} # empty dictionary 

statuses = ["active", "completed", "pending"]

count = 0

for plist in projects.values():
    for p in plist:
        p["status"] = statuses[count % 3]
        
        status = p["status"]
        status_counts[status] = status_counts.get(status, 0) + 1
        count += 1 

print("\n\nProject Status Summary:")
print("-" * 60)
print(status_counts)

# TODO 19: Budget analysis function with aggregation
def analyze_customer_budgets(projects_dict):
    results = {}
    
    for cid, plist in projects_dict.items():
        budgets = [p["budget"] for p in plist]
        
        total = sum(budgets)
        count = len(budgets)
        avg = total / count if count > 0 else 0
        
        results[cid] = {"total": total, "average": avg, "count": count}
        
    return results

print("\n\nDetailed Budget Analysis:")
print("-" * 60)

analysis = analyze_customer_budgets(projects)
print(analysis)

# TODO 20: Service recommendation system
def recommend_services(customer_id, customers, projects, services):
    
    used_services = []
    
    if customer_id in projects:
        for p in projects[customer_id]:
            used_services.append(p["service"])
            
    recommendations = []
    
    for service in services:
        if service not in used_services:
            recommendations.append(service)
            
    return recommendations

print("\n\nService Recommendations:")
print("-" * 60)

for cid in customers:
    rec = recommend_services(cid, customers, projects, services)
    print(cid, "recommended services:", rec) 