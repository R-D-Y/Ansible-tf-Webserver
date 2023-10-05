# Ansible and Terraform to make Webserver on cloud

## Working with Ansible and Terraform (on Azure Cloud)

This repository provides automation scripts for deploying a static HTML page on Azure virtual machines using Ansible and Terraform.

### Files:

- `HTML-PAGE-NODE-1.html`: Static HTML page for Node1
- `HTML-PAGE-NODE-2.html`: Static HTML page for Node2
- `1node.yml`: Ansible playbook that updates the VM, installs Nginx, and deploys HTML 1 as the front page
- `2node.yml`: Ansible playbook that updates the VM, installs Nginx, and deploys HTML 2 as the front page
- `main.tf`: Terraform file providing resources
- `network.tf`: Terraform file providing network resources
- `config.yaml`: Mapping for personalized parameters
- `*.tf` and `*.yaml`: More Terraform and configuration files will be made available soon.

### Project Description:

1. Launch Terraform to create two virtual machines on Azure.
2. After the VMs are created, extract their public IP addresses and update `inventory.ini` in Ansible with these IPs.
3. Run the Ansible playbooks which will update the virtual machines, install Nginx, and fetch the HTML pages from a GitHub repository to display them on the VMs.

## Getting Started 

1. Clone the repository:

```plaintext
git clone https://github.com/R-D-Y/HAnsible-tf-Webserver.git
```


2. Navigate to the project directory:

```plaintext
cd your-repo
```


3. Initialize Terraform:

```plaintext
terraform init
```


4. Review and modify the Terraform configuration files according to your requirements. (Like your subscription ID for example)

5. Creates an execution plan:

```plaintext
terraform plan
```

6. Deploy the infrastructure:

```plaintext
terraform apply
```

7. Once terraform is launch, put vm ip's on `inventory.ini`

8. Run the Ansible playbook to deploy the web server and configure the VMs:

```plaintext
ansible-playbook 1node.yml
ansible-playbook 2node.yml
```


## Cleanup
To remove the deployed infrastructure, run:

```plaintext
terraform destroy --auto-approve
```

**Note:** This will permanently delete all resources created by this project.

# License
This project is licensed under the MIT License.
