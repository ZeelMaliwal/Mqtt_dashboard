# MQTT Dashboard - Django Web App for IoT Sensor Data  

## Overview  
This project is a Django-based **MQTT dashboard** that connects to **The Things Network (TTN)** using MQTT to receive and process **temperature and humidity** data from IoT sensors. The received data is stored in a database and can be used for real-time monitoring.  

## Features  
✅ **Real-time IoT data monitoring** using MQTT  
✅ **Data storage** in Django models  
✅ **Secure communication** with TTN using TLS  
✅ **Test message simulation** for debugging  

## ⚙️ Setup & Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/mqtt_dashboard.git
cd mqtt_dashboard
```

### **2️⃣ Create a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **4️⃣ Configure MQTT Credentials**  
The MQTT broker details and credentials are **hardcoded** inside the following files:  
- **`mqtt_client.py`** (For receiving data)  
- **`publish_test_message.py`** (For sending test data)  

Before running the project, **update these files** with your correct **APPID**, **Password**, and **MQTT topic**.

Example inside `mqtt_client.py`:
```python
APPID = "your_appid@ttn"
PSW = "your_password"
```

Example inside `publish_test_message.py`:
```python
username = "your_appid@ttn"
password = "your_password"
topic = "v3/lairdtemphum@ttn/devices/your_device_id/up"
```

### **5️⃣ Run Django Migrations**  
```bash
python manage.py migrate
```

### **6️⃣ Start the MQTT Client**  
```bash
python manage.py mqtt_client
```

### **7️⃣ Run the Django Development Server**  
```bash
python manage.py runserver
```

## MQTT Broker Configuration  
- Broker: `eu1.cloud.thethings.network`  
- Port: `8883` (TLS secure connection)  
- Topic: `v3/lairdtemphum@ttn/devices/+/up`  

## Simulating Data (Testing)  
To test the MQTT setup, run:  
```bash
python publish_test_message.py
```

## Important Notes  
- This project is designed for **IoT applications**, such as:  
  - **Smart agriculture** (monitoring temperature & humidity in farms).  
  - **Home automation** (tracking environmental conditions).  
  - **Industrial monitoring** (real-time factory conditions).  

## 📝 License  
This project is licensed under the MIT License.  

---

