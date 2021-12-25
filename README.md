# Kubernetes-Managing-Storage

**1- Using emptyDir for intra-pod communication**

**Usage**:
  - To share data between containers in the same pod using a shared volume.
It is not Persistent , if pod removed from node, the contents are erased.
__________________________________________________________________________
**2- Using HostPath for intra-node communication**

**Usage**:

  - If you want pods to get access to some host information or you want pods on the same node to communicate with each other (DaemonSet, Pod affinity, single node, etc )
It is not persistent in case of pod restarts and node restarts   
___________________________________________________________________________
**3- Using local volumes for durable node storage**

**Usage**:
  - Local volumes are similar to HostPath, but they persist across pod restarts and node restarts. In that sense, they are considered persistent volumes
  - It is used to support StatefulSets where specific pods need to be scheduled on nodes that contain specific storage volumes
  - Local volumes should have node affinity annotations. 
  - StorageClass needed in order to use local volumes.
____________________________________________________________________________

