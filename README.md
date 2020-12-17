# Define your config file:

Use the example below as reference:
```bash
cat << EOF > config.yml
---

  root_pw_hash: #PWD_HASH#
  # To generate a password hash:
  # python3 -c 'import crypt; import os; print(crypt.crypt("root_password", crypt.mksalt(crypt.METHOD_SHA512)))'


  authorized_keys: 
    - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC4tzrayU6ahMhmWuicy+oFfy//9oB+2EdbbmDfA0d+k3SpYjWVqho64/L+sQIAN0RGBJx42GkbKi8B6AriPw8omLOCk2WSYW3ymEC7n3l32M5T4cLr8LIYwoMOBZkMtRc3H62PrHgDoTJLhUOvT2ewj1SLl7iU5gQuInwPE6jWooIb8R6KMUl31qNpkafCVPz5ovw0iYbDamHQF6sq081Xl39px2345T8TofIAocyBUfCOstmAvPaD9lXIV3j9JmPhAy0oweXpxdPiQzBHXepLh/jrvHrV5ggl2iwmLgF3uzwYdFlQN6eCniBtBEcGqEacb6oP2KHfHer04WIbAMHZ eduardoefb@efb
    - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDEogQQvxuvrZQZY7mNRxWTQ2KM+BzggtaGbckhevJiOXHbN1TyJZNFXMHz3ZH2g913uXCD31hikSwhWQdGPDCIy8KRPdaDsa9zVhZJ5e/WQ9/g2OYaZDlL1ESQtJvCCubo7XDxHkOPxrjaIJrt8sAJRCBO3GIoY+Ush+tqG7KnGuj3Z9MkunaRmNKmaOrRQtxAhGW0na6mRltdpkdVvSrER1MIh4dipr6CAm79xcdqzq64qkYLPq31AQs8A4B8rIPcZipaxBFi5KARC9PvEJ4pkAvaGFnPmFY1v1FUGSsuF0hRZiqa/gUU1QGKvT2UlA1dvbU6gY2rohilMiDtQOaD eduardoefb@efb
  
  
  timezone: Brazil/East
  hypervisor:
    name: hypervisor
    ip: 10.2.1.31
    workdir: /srv/lab     
  
  network:
    domain: openstack.int
    ntp_servers:
      - 10.2.1.1
      #- 0.centos.pool.ntp.org
      #- 1.centos.pool.ntp.org
      #- 2.centos.pool.ntp.org
      #- 3.centos.pool.ntp.org
      
    oam:
      name: lab_oam
      external_vlan: 60
      external_interface: eth0
      network: 10.6.0.0
      broadcast: 10.6.0.255
      gateway: 10.6.0.1
      netmask: 255.255.255.0
      netmask_len: 24
      dns: 8.8.8.8
      dev: "vnet0"
      alias: "net0"
      slot: "0x10"
      type: "rtl8139"
 
    external:
      - name: extnet01
        external_vlan: 62
        external_interface: eth1
        network: 10.7.0.0        
        broadcast: 10.7.0.255        
        netmask: 255.255.255.0
        netmask_len: 24
        dev: "vnet1"
        alias: "net1"
        slot: "0x11" 
        type: "rtl8139"   

      - name: extnet02
        external_vlan: 63
        external_interface: eth2
        network: 10.8.0.0        
        broadcast: 10.8.0.255        
        netmask: 255.255.255.0
        netmask_len: 24
        dev: "vnet2"
        alias: "net2"
        slot: "0x12" 
        type: "rtl8139"          

  iso_image:
    url: http://ftp.unicamp.br/pub/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-2009.iso
    #url: http://10.2.1.32/images/CentOS-7-x86_64-Minimal-2009.iso
    filename: centos_7.iso

  nodes:  
    - name: controller01
      hypervisor: "{{ hypervisor }}"
      ram: 8192000
      cpus: 4      
      disk: 
        - name: "controller01_disk_0.qcow2"
          size: "40G"
          dev: "sda"
          unit: 1
          bus: "sata"
      oam_ip: "10.6.0.10"      
      external_ips:
        - 10.7.0.10
        - 10.8.0.10
		
      vnc: 
        port: 26010

    - name: compute01
      hypervisor: "{{ hypervisor }}"
      ram: 8192000
      cpus: 4       
      disk: 
        - name: "compute01_disk_0.qcow2"
          size: "40G"
          dev: "sda"
          unit: 1
          bus: "sata"
      oam_ip: "10.6.0.20"      
      external_ips:
        - 10.7.0.20
        - 10.8.0.20

      vnc: 
        port: 26020   

    - name: compute02
      hypervisor: "{{ hypervisor }}"
      ram: 8192000
      cpus: 4       
      disk: 
        - name: "compute02_disk_0.qcow2"
          size: "40G"
          dev: "sda"
          unit: 1
          bus: "sata"
      oam_ip: "10.6.0.21"      
      external_ips:
        - 10.7.0.21
        - 10.8.0.21
      
      vnc: 
        port: 26021  
        
    - name: compute03
      hypervisor: "{{ hypervisor }}"
      ram: 8192000
      cpus: 4       
      disk: 
        - name: "compute03_disk_0.qcow2"
          size: "40G"
          dev: "sda"
          unit: 1
          bus: "sata"
      oam_ip: "10.6.0.22"      
      external_ips:
        - 10.7.0.22
        - 10.8.0.22
      
      vnc: 
        port: 26022        
                
    - name: storage01
      hypervisor: "{{ hypervisor }}"
      ram: 8192000
      cpus: 4      
      disk: 
        - name: "storage01_disk_0.qcow2"
          size: "40G"
          dev: "sda"
          unit: 1
          bus: "sata"
        - name: "storage01_disk_1.qcow2"
          size: "40G"
          dev: "sdb"
          unit: 2
          bus: "sata"          
      oam_ip: "10.6.0.30"      
      external_ips:
        - 10.7.0.30
        - 10.8.0.30
      
      vnc: 
        port: 26030     


    - name: storage02
      hypervisor: "{{ hypervisor }}"
      ram: 8192000
      cpus: 4      
      disk: 
        - name: "storage02_disk_0.qcow2"
          size: "40G"
          dev: "sda"
          unit: 1
          bus: "sata"
        - name: "storage02_disk_1.qcow2"
          size: "40G"
          dev: "sdb"
          unit: 2
          bus: "sata"          
      oam_ip: "10.6.0.31"      
      external_ips:
        - 10.7.0.31
        - 10.8.0.31
      
      vnc: 
        port: 26031


  # Obs.: The openstack variable is only needed for openstack deployment
  openstack:                
    controller:
      ip: 10.6.0.10
      name: controllervip
      
    provider_networks:
      - name: extnet01
        device: eth1
        gateway: 10.7.0.1
        range_begin: 10.7.0.100
        range_end: 10.7.0.200

      - name: extnet02
        device: eth2
        gateway: 10.8.0.1
        range_begin: 10.8.0.100
        range_end: 10.8.0.200        
    
    cinder:
       volume_name: cinder_volumes
       volume_device: sdb    
EOF
```

# Create your enviroment:

You can crete your inventory manually or using the python script, that will extract the nodes from config.yml:

Option 1: Using the python script
```bash
python3 create_inventory.py config.yml
```

Option 2: Creating the infentory file manually (example)
```bash
cat << EOF > hosts
[controller]
10.6.0.10

[compute]
10.6.0.20
10.6.0.21
10.6.0.22

[storage]
10.6.0.30
10.6.0.31

[controller01]
10.6.0.10

[compute01]
10.6.0.20

[compute02]
10.6.0.21

[compute03]
10.6.0.22

[storage01]
10.6.0.30

[storage02]
10.6.0.31
EOF
```

# Start openstack installation:
```bash
time ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i hosts create.yml 
```

# Once openstack is installed, execute the following steps to validate the installation (connect to the controller node as root):

1 - Create a private key file:
```bash
ssh-keygen -q -N ""
```
2 - Create a flavor:
```bash
. admin-openrc
openstack flavor create --id 0 --vcpus 1 --ram 64 --disk 1 m1.nano
```

3 - Create a provider network:
```bash
. admin-openrc
openstack network create  --share --external \
  --provider-physical-network extnet01 \
  --provider-network-type flat extnet01

openstack subnet create --network extnet01 \
  --allocation-pool start=10.7.0.100,end=10.7.0.200 \
  --dns-nameserver 8.8.8.8 --gateway 10.7.0.1 \
  --subnet-range 10.7.0.0/24 extnet01  
```

4 - Create the keypair and security group as demo user
```bash
. demo-openrc
openstack keypair create --public-key ~/.ssh/id_rsa.pub mykey
openstack keypair list
openstack security group rule create --proto icmp default
openstack security group rule create --proto tcp --dst-port 22 default
```

5 - Create a provider instance:
```bash
openstack server create --flavor m1.nano --image cirros \
  --nic net-id=`openstack network show extnet01 -c id | grep " id " | awk '{print $4}'` --security-group default \
  --key-name mykey provider-instance
openstack server list  
```

6 - Create a self service networ, router and instance:
```bash
openstack network create selfservice
openstack subnet create --network selfservice \
  --dns-nameserver 8.8.8.8 --gateway 172.31.0.1 \
  --subnet-range 172.31.0.0/24 selfservice
  
openstack router create router
openstack router add subnet router selfservice
openstack router set router --external-gateway extnet01

openstack server create --flavor m1.nano --image cirros \
  --nic net-id=`openstack network show selfservice -c id | grep " id " | awk '{print $4}'` --security-group default \
  --key-name mykey selfservice-instance
openstack server list  
openstack console log show selfservice-instance
```

7 - Create a floating IP and add to self service instance:
```bash
openstack floating ip create extnet01
openstack server add floating ip selfservice-instance 10.7.0.169
openstack server list  
```

8 - Test cinder volumes:
```bash
openstack volume create --size 1 volume1
openstack volume create --size 1 volume2
openstack volume list
openstack server add volume provider-instance volume1
openstack server add volume selfservice-instance volume2
openstack volume list
```

9 - Test heat (orchestration):
```bash

cat << EOF > heat-demo.yml
heat_template_version: 2015-10-15
description: Launch a basic instance with CirrOS image using the
             ``m1.tiny`` flavor, ``mykey`` key,  and one network.

parameters:
  NetID:
    type: string
    description: Network ID to use for the instance.

resources:
  server:
    type: OS::Nova::Server
    properties:
      image: cirros
      flavor: m1.nano
      key_name: mykey
      networks:
      - network: { get_param: NetID }

outputs:
  instance_name:
    description: Name of the instance.
    value: { get_attr: [ server, name ] }
  instance_ip:
    description: IP address of the instance.
    value: { get_attr: [ server, first_address ] }
EOF

export NET_ID=$(openstack network list | awk '/ extnet01 / { print $2 }') && echo $NET_ID
openstack stack create -t heat-demo.yml --parameter "NetID=$NET_ID" stack
openstack stack list
openstack server list
```