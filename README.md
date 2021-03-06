# Kubernetes-Managing-Storage  "Proof of concept"

**1- Using emptyDir for intra-pod communication &nbsp;&nbsp;&nbsp;&nbsp;Ref-->emptyDir**

**Usage**:
  - To share data between containers in the same pod using a shared volume.
It is not Persistent , if pod removed from node, the contents are erased.
__________________________________________________________________________

**2- Using HostPath for intra-node communication &nbsp;&nbsp;&nbsp;&nbsp;Ref-->hostPath**

**Usage**:

  - If you want pods to get access to some host information or you want pods on the same node to communicate with each other (DaemonSet, Pod affinity, single node, etc )
It is not persistent in case of pod restarts and node restarts   
___________________________________________________________________________

**3- Using local volumes for durable node storage  &nbsp;&nbsp;&nbsp;&nbsp;Ref-->persistent-local-volume**

**Usage**:
  - Local volumes are similar to HostPath, but they persist across pod restarts and node restarts. In that sense, they are considered persistent volumes
  - It is used to support StatefulSets where specific pods need to be scheduled on nodes that contain specific storage volumes
  - Local volumes should have node affinity annotations. 
  - StorageClass needed in order to use local volumes.
____________________________________________________________________________

**4- Provisioning persistent volumes using DirectNFS   &nbsp;&nbsp;&nbsp;&nbsp;Ref-->directNFS**

**Usage**:
 - It is good to move storage provisioners out of Kubernetes core into volume plugins ( NFS in this case )
____________________________________________________________________________

**5- Amazon EBS  &nbsp;&nbsp;&nbsp;&nbsp;Ref-->Amazon-EBS** 

**Limitations**:
  - Nodes should be AWS EC2 instances.
  - Pods can only access EBS volumes in the same availability zone.
  - EBS Volume can be mounted only on one node.
  - Pods can not share the same EBS Volume unless they run on the same node.

**Note** that no need for a claim or storage class , we only mount the volume directly by ID
_____________________________________________________________________________

**6- Amazon EFS &nbsp;&nbsp;&nbsp;&nbsp;Ref-->Amazon-EFS**
 - Managed NFS service and does not have the limitations of Amazon EBS but could be more expensive.
 - External provisioner needed in order to allow you to mount EFS storage as PersistentVolumes in kubernetes.
 - The pv/pvc config pretty similar to NFSdirect.

**Note    the EFS provisioner is not covered here!**
_____________________________________________________________________________

**7- gcePersistentDiskR &nbsp;&nbsp;&nbsp;&nbsp;Ref-->gcePersistentDisk**

**Limitations**:
  - It can only be used by GCE instances in the same project and zone.

**Usage**:
  - it supports ReadWriteOnce and ReadOnlyMany. You can use it to share data as read-only between multiple pods in the same zone.

_____________________________________________________________________________

**8- Azure Files &nbsp;&nbsp;&nbsp;&nbsp;Ref-->AzureFiles**
  - Azure Files uses the SMB/CIFS protocol 
  - In order to use Azure File you need to create a secret contains 
              - azurestorageaccountname
              - azurestorageaccountkey

