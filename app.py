import requests
import time
import random

URL = "http://cloud.emeautomation.com:8080/api/v1/zHilOUHyoGcXk55aWsg9/telemetry"

def generate_data():
return {
"sd_atmr_rpm": random.randint(1400, 1500),
"sd_feed_pump_rpm": random.randint(1100, 1300),
"sd_inlet_temp": round(random.uniform(80, 90), 2),
"sd_outlet_temp": round(random.uniform(90, 100), 2),
"sd_fdb_rpm": random.randint(1300, 1400),
"sd_idb_rpm": random.randint(1300, 1400),
"sfd_fdb_rpm": random.randint(1350, 1450),
"ps_rpm": random.randint(1000, 1200),
"ph_rpm": random.randint(1100, 1200),
"sfd_idb_rpm": random.randint(1350, 1450),
"sa_rpm": random.randint(1200, 1300),
"sf_rpm": random.randint(1250, 1350),
"sfd_outlet_temp": round(random.uniform(90, 100), 2),
"sfd_inlet_temp": round(random.uniform(85, 95), 2)
}

while True:
try:
data = generate_data()
r = requests.post(URL, json=data)
print("Sent:", data, "Status:", r.status_code)
except Exception as e:
print("Error:", e)

```
time.sleep(30)
```
