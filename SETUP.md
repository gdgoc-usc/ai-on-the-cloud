# Cloud Account Setup Guide

This guide will walk you through setting up both Google Cloud Platform (GCP) and Amazon Web Services (AWS) accounts for the AI on the Cloud training event.

## Table of Contents
- [GCP Account Setup](#gcp-account-setup)
- [AWS Account Setup](#aws-account-setup)
- [Next Steps](#next-steps)

---

## GCP Account Setup

### Prerequisites
- A valid email address (Gmail recommended)
- A valid credit/debit card (for identity verification)
- Phone number for verification

### Step 1: Create Your GCP Account

1. **Navigate to GCP Console**
   - Go to [https://cloud.google.com/](https://cloud.google.com/)
   - Click on **"Get started for free"** or **"Start free"**

2. **Sign in with Google Account**
   - Use an existing Google account or create a new one
   - Follow the prompts to sign in

3. **Complete Account Setup**
   - **Country**: Select your country
   - **Terms of Service**: Read and accept the Terms of Service
   - Click **"Continue"**

4. **Enter Payment Information**
   - Provide your credit/debit card details
   - Note: You won't be charged unless you upgrade to a paid account
   - Complete the identity verification process

5. **Verify Your Phone Number**
   - Enter your phone number
   - Enter the verification code sent via SMS

### Step 2: Understanding GCP Free Tier

Google Cloud offers a generous free tier:
- **$300 in free credits** valid for 90 days for new users
- **Always Free tier** with limited usage of popular services:
  - Compute Engine: 1 f1-micro instance per month
  - Cloud Storage: 5GB per month
  - BigQuery: 1TB of querying per month
  - And more...

### Step 3: Set Up Your First Project

1. **Navigate to Console**
   - Go to [https://console.cloud.google.com/](https://console.cloud.google.com/)

2. **Create a New Project**
   - Click on the project dropdown at the top
   - Click **"New Project"**
   - Enter a project name (e.g., "AI-Training-Project")
   - Click **"Create"**

3. **Note Your Project ID**
   - Your project ID is unique and will be used for API calls
   - Find it in the project dropdown or dashboard

### Step 4: Enable Required APIs

For AI/ML workloads, you may need to enable:

1. **Navigate to APIs & Services**
   - From the hamburger menu (☰), go to **"APIs & Services"** → **"Library"**

2. **Enable Common APIs**
   - Search for and enable:
     - **Vertex AI API** (for ML workloads)
     - **Compute Engine API** (for VM instances)
     - **Cloud Storage API** (for data storage)
     - **Cloud Functions API** (for serverless computing)

### Step 5: Set Up Billing Alerts

Protect yourself from unexpected charges:

1. **Navigate to Billing**
   - Go to **"Billing"** from the hamburger menu
   - Select your billing account

2. **Create a Budget**
   - Click **"Budgets & alerts"** in the left sidebar
   - Click **"Create Budget"**
   - Set a budget amount (e.g., $50)
   - Configure alert thresholds (50%, 90%, 100%)
   - Add your email for notifications

### Step 6: Install Google Cloud CLI (Optional)

For command-line access:

1. **Download gcloud CLI**
   - Visit [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
   - Download the installer for your OS

2. **Initialize gcloud**
   ```bash
   gcloud init
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

---

## AWS Account Setup

### Prerequisites
- A valid email address
- A valid credit/debit card (for identity verification)
- Phone number for verification

### Step 1: Create Your AWS Account

1. **Navigate to AWS**
   - Go to [https://aws.amazon.com/](https://aws.amazon.com/)
   - Click **"Create an AWS Account"** (top right corner)

2. **Enter Account Information**
   - **Email address**: Enter your email
   - **AWS account name**: Choose a name for your account
   - Click **"Verify email address"**

3. **Verify Your Email**
   - Check your email for a verification code
   - Enter the verification code
   - Click **"Verify"**

4. **Create Password**
   - Enter a strong password
   - Confirm the password
   - Click **"Continue"**

5. **Contact Information**
   - Select account type: **Personal** or **Professional**
   - Enter your full name, phone number, and address
   - Read and accept the AWS Customer Agreement
   - Click **"Continue"**

6. **Payment Information**
   - Enter your credit/debit card details
   - Note: You won't be charged unless you exceed free tier limits
   - Click **"Verify and Continue"**

7. **Identity Verification**
   - Select phone call or SMS verification
   - Enter the verification code displayed on screen when prompted
   - Click **"Continue"**

8. **Select Support Plan**
   - Choose **"Basic support - Free"** (recommended for learning)
   - Click **"Complete sign up"**

### Step 2: Understanding AWS Free Tier

AWS offers three types of free tier:

1. **12 Months Free** (from account creation):
   - EC2: 750 hours per month of t2.micro instances
   - S3: 5GB of standard storage
   - RDS: 750 hours per month of db.t2.micro instances
   - Lambda: 1 million free requests per month
   - And more...

2. **Always Free**:
   - Lambda: 1 million requests per month (forever)
   - DynamoDB: 25GB of storage
   - SNS: 1 million publishes per month
   - And more...

3. **Free Trials**:
   - SageMaker: 2 months free trial
   - Comprehend: 12 months free trial
   - And more...

### Step 3: Access the AWS Management Console

1. **Sign In to Console**
   - Go to [https://console.aws.amazon.com/](https://console.aws.amazon.com/)
   - Click **"Sign in to the Console"**
   - Enter your email and password

2. **Explore the Console**
   - Familiarize yourself with the service search bar
   - Note the region selector (top right) - choose a region close to you

### Step 4: Set Up IAM Security

Secure your root account and create an IAM user:

1. **Enable MFA on Root Account**
   - Click on your account name (top right)
   - Click **"Security credentials"**
   - Scroll to **"Multi-factor authentication (MFA)"**
   - Click **"Assign MFA device"** and follow instructions

2. **Create an IAM User**
   - Search for **"IAM"** in the services search
   - Click **"Users"** in the left sidebar
   - Click **"Add users"**
   - Enter a username (e.g., "admin-user")
   - Select **"Programmatic access"** and **"AWS Management Console access"**
   - Set permissions: Attach **"AdministratorAccess"** policy for now
   - Complete the wizard and save the credentials

3. **Use IAM User for Daily Operations**
   - Sign out of the root account
   - Sign in using the IAM user credentials
   - URL: `https://YOUR_ACCOUNT_ID.signin.aws.amazon.com/console`

### Step 5: Set Up Billing Alerts

Protect yourself from unexpected charges:

1. **Enable Billing Alerts**
   - Click on your account name (top right)
   - Click **"Billing and Cost Management"**
   - Click **"Billing preferences"** in the left sidebar
   - Check **"Receive Billing Alerts"**
   - Check **"Receive Free Tier Usage Alerts"**
   - Enter your email address
   - Click **"Save preferences"**

2. **Create a CloudWatch Billing Alarm**
   - Switch region to **US East (N. Virginia)** (billing metrics are only available here)
   - Search for **"CloudWatch"** service
   - Click **"Alarms"** → **"All alarms"**
   - Click **"Create alarm"**
   - Click **"Select metric"**
   - Choose **"Billing"** → **"Total Estimated Charge"**
   - Select **USD** checkbox and click **"Select metric"**
   - Set threshold amount (e.g., $10)
   - Configure SNS notification with your email
   - Complete the alarm creation

### Step 6: Install AWS CLI (Optional)

For command-line access:

1. **Download AWS CLI**
   - Visit [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)
   - Download the installer for your OS

2. **Configure AWS CLI**
   ```bash
   aws configure
   ```
   - Enter your Access Key ID
   - Enter your Secret Access Key
   - Enter default region (e.g., us-east-1)
   - Enter default output format (json)

---

## Next Steps

### After Setup
1. **Familiarize Yourself with Consoles**
   - Explore the GCP Console and AWS Management Console
   - Understand where different services are located

2. **Review Free Tier Limits**
   - Keep track of your usage to avoid unexpected charges
   - Set up alerts as described above

3. **Explore AI/ML Services**
   - **GCP**: Vertex AI, AutoML, BigQuery ML
   - **AWS**: SageMaker, Comprehend, Rekognition

4. **Review Documentation**
   - [GCP Documentation](https://cloud.google.com/docs)
   - [AWS Documentation](https://docs.aws.amazon.com/)

### Important Notes
- ⚠️ **Always monitor your billing**: Check your billing dashboard regularly
- ⚠️ **Clean up resources**: Delete resources you're not using to avoid charges
- ⚠️ **Use free tier wisely**: Both platforms offer generous free tiers, but they have limits
- 🔒 **Security first**: Enable MFA and follow security best practices
- 💡 **Start small**: Begin with simple projects before moving to complex deployments

### Troubleshooting

**GCP Issues**:
- If you can't create a project, ensure billing is enabled
- If APIs aren't working, make sure they're enabled in the API Library

**AWS Issues**:
- If you can't access services, check your IAM permissions
- If billing alerts aren't working, ensure you're in the US East (N. Virginia) region for CloudWatch billing metrics

### Support Resources
- **GCP Support**: [Google Cloud Support](https://cloud.google.com/support)
- **AWS Support**: [AWS Support](https://aws.amazon.com/support)
- **Community Forums**:
  - [GCP Community](https://www.googlecloudcommunity.com/)
  - [AWS Forums](https://forums.aws.amazon.com/)

---

**Ready to start your cloud AI journey!** 🚀

If you encounter any issues during setup, please reach out to the course instructors or refer to the official documentation linked throughout this guide.
