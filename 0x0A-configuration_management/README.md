**Puppet** to **Configuration** is **Makefile** to **Compilation** <br/>
<br/>
As we write some instructions in the makefile files, we also write some instructions in the puppet files to make the configuration management easier, reliable, scalable.
<br/>
<br/>
There are two main components in **Puppet**:

1. The Master
2. The Client (The Slave)
   <br/>
   <br/>

**The Master**:
<br/>

- Is the central server that controlling the configuration management process and contains the Puppet manifests and distributing them to the Puppet clients.

**The Client**:
<br/>

- Are the nodes (servers, workstations, devices) that are managed by Puppet, they are contacting with the master Puppet to request the manifests to make sure that the current node's state is the required one as described in the manifest, and then send back a report to the master with the current stat.
  <br/>
  I think that, this process is happens every 30 minutes.
