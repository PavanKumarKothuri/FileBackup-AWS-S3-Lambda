# 🚀 Simple File Backup System with AWS Lambda & S3

![Project Thumbnail](https://github.com/PavanKumarKothuri/FileBackup-AWS-S3-Lambda/FileBackupThumbnail.webp)

## 🗂️ Automate Your Backups Like a Pro!

This project demonstrates how to automate file backups between S3 buckets using AWS Lambda. It's a simple, cost-effective solution for ensuring your data is always safe and secure. 💡 Whether you're a freelancer looking to impress clients or a business needing reliable backups, this project is your gateway to effortless automation!

---

## **💻 The Problem**

Data loss is a nightmare! Businesses often struggle with:

- 🔄 Manually backing up files (time-consuming and error-prone).
- 🔒 Ensuring critical files are safely stored in redundant locations.
- 💸 Avoiding expensive backup solutions.

---

## **🎯 The Solution**

**Simple File Backup System** automates this process by:

1. Detecting new files uploaded to a **Source S3 Bucket**.
2. Automatically copying them to a **Destination S3 Bucket** for backup.
3. Leveraging **AWS Lambda** and **S3 Events**, ensuring a serverless, pay-as-you-go architecture.

### **✨ Benefits**

- **⚙️ Fully Automated**: Zero manual effort.
- **📈 Scalable**: Handles any number of files without extra setup.
- **💰 Cost-Effective**: No need for expensive third-party tools.

---

## **🛠️ Technical Implementation**

This project uses:

1. **AWS Lambda**: A serverless function triggered when a file is uploaded to the source bucket.
2. **S3 Event Notifications**: Triggers the Lambda function upon file creation in the source bucket.
3. **Python (Boto3 SDK)**: Handles interactions between Lambda and S3 buckets.

---

### **📝 Project Structure**

```
.
├── lambda_function.py      # Core Lambda function code
├── test_event.json         # Sample event for local testing
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

### **👩‍💻 Code Walkthrough**

```python
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Parse bucket and file details from the event
    source_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    file_key = event["Records"][0]["s3"]["object"]["key"]
    destination_bucket = "destination-bucket-yourname"
    
    s3 = boto3.client("s3")
    
    try:
        # Copy file from source to destination bucket
        logger.info(f"Copying {file_key} from {source_bucket} to {destination_bucket}")
        s3.copy_object(
            Bucket=destination_bucket,
            CopySource={"Bucket": source_bucket, "Key": file_key},
            Key=file_key,
        )
        logger.info(f"Backup successful: {file_key}")
        return {"status": "success", "message": f"{file_key} backed up successfully."}
    except Exception as e:
        logger.error(f"Error during backup: {e}")
        return {"status": "error", "message": str(e)}
```

---

## **🚀 How to Use**

### **1. Deploy the Lambda Function**

1. Create a Lambda function in the AWS Console.
2. Paste the code from `lambda_function.py`.
3. Attach the `AmazonS3FullAccess` policy to the Lambda execution role.

### **2. Configure S3 Buckets**

1. Create a **source bucket** and a **destination bucket** in the AWS S3 Console.
2. Set up an S3 event notification on the source bucket to trigger the Lambda function.

### **3. Test the System**

1. Upload a file to the source bucket.
2. Check the destination bucket to confirm the file has been backed up.

---

## **🌟 Challenges & How We Solved Them**

1. **S3 Bucket Configuration**: Ensured bucket names are region-specific and correctly matched.
2. **Lambda Permissions**: Attached proper IAM policies to allow access to both S3 buckets.
3. **Testing Locally**: Simulated S3 events using a `test_event.json` file to debug efficiently.

---

## **📊 Business Impact**

- **⏳ Saves Time**: Automates routine backup tasks, freeing up valuable hours.
- **🔐 Ensures Reliability**: Critical data is backed up securely in near real-time.
- **💡 Scales with Business Growth**: Handles large file volumes without additional infrastructure.

---

## **📚 Learnings**

- Working with serverless architectures (AWS Lambda).
- Implementing event-driven programming using S3 Event Notifications.
- Handling real-world scenarios like permission errors and region mismatches.

---

## **🚀 Get Started Today**

Backup your files effortlessly with this **Simple File Backup System**! Have questions or need help? Open an issue or reach out. 😊

---

## **🏆📫 Author**

- Built with ❤️ by PavanKumar Kothuri - Passionate about Cloud Computing, CyberSecurity and Machine learning!
- 🌐 [LinkedIn | https://www.linkedin.com/in/iamkpk/](https://www.linkedin.com/in/iamkpk/)
- 💻 [GitHub | https://github.com/PavanKumarKothuri](https://github.com/PavanKumarKothuri)  
- ✉️ [Email | pavankumarkothuri9@gmail.com](mailto:pavankumarkothuri9@gmail.com)

Feel free to connect with me for further discussions or contributions. 🌟 **Happy Coding!** 🚀
