# Kubernetes-Managing-Storage  "Proof of concept"

**1- Using emptyDir for intra-pod communication      Ref-->emptyDir**

**Usage**:
  - To share data between containers in the same pod using a shared volume.
It is not Persistent , if pod removed from node, the contents are erased.
__________________________________________________________________________
**2- Using HostPath for intra-node communication     Ref-->hostPath**

**Usage**:

  - If you want pods to get access to some host information or you want pods on the same node to communicate with each other (DaemonSet, Pod affinity, single node, etc )
It is not persistent in case of pod restarts and node restarts   
___________________________________________________________________________
**3- Using local volumes for durable node storage     Ref-->persistent-local-volume**

**Usage**:
  - Local volumes are similar to HostPath, but they persist across pod restarts and node restarts. In that sense, they are considered persistent volumes
  - It is used to support StatefulSets where specific pods need to be scheduled on nodes that contain specific storage volumes
  - Local volumes should have node affinity annotations. 
  - StorageClass needed in order to use local volumes.
____________________________________________________________________________
**4- Provisioning persistent volumes using DirectNFS   Ref-->directNFS**

**Usage**:
 - It is good to move storage provisioners out of Kubernetes core into volume plugins ( NFS in this case )
____________________________________________________________________________
**5- Amazon EBS    Ref-->Amazon-EBS** 

**Limitations**:
  - Nodes should be AWS EC2 instances.
  - Pods can only access EBS volumes in the same availability zone.
  - EBS Volume can be mounted only on one node.
  - Pods can not share the same EBS Volume unless they run on the same node.

**Note** that no need for a claim or storage class , we only mount the volume directly by ID
_____________________________________________________________________________
