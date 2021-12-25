# Kubernetes-Managing-Storage

**1- Using emptyDir for intra-pod communication**

**Usage:
  - To share data between containers in the same pod using a shared volume.
It is not Persistent , if pod removed from node, the contents are erased.
__________________________________________________________________________
**2- Using HostPath for intra-node communication**

**Usage:
  -If you want pods to get access to some host information or you want pods on the same node to communicate with each other (DaemonSet, Pod affinity, single node, etc )
It is not persistent in case of pod restarts and node restarts   

