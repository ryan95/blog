# Ryan Stephens
# theazureblog.co.uk


# Update
yum -y update

# Install Git

yum -y install git

# Create ansible repo file

cat >/etc/yum.repos.d/ansible.repo <<EOL
[ansible-release]
name=Ansible Release
baseurl=https://releases.ansible.com/ansible/rpm/release/epel-7-x86_64/
gpgcheck=0
EOL


# Install Ansible

yum -y install ansible

# Install Python Package Manager Pip
curl -s https://bootstrap.pypa.io/get-pip.py | python


# Upgrade cryptography - required for CREDSSP

pip install cryptography --upgrade


# Install pywinrm - required for configuring Windows Servers
pip install pywinrm


# Install requests credssp - required for configuring windows servers over CREDSSP

pip install requests-credssp