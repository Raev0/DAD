
>This project is about a tool making sure other process(node service process deployed on windows server 2012). this application is just running like this:


![](https://github.com/Raev0/DAD/blob/master/DAD_02_ProcessWatcher/images/processshow.png)
---
How to use it:

- All framework support required is the .net framework 4.5

- Copy the demo folder into the `directory` of `E:\work`. if you want to customize this directory, please modify both the `processWacher.cpp` together with the `recovery.bat`
- Running the `ffs-node-server.exe` and `node.exe` first(of course they are fake). then click the `processWatcher.exe` 
- You wouldn't see a dog in the Task Manager but see the `processWatcher.exe` ; then you will never shut down `ffs-node-server.exe` and `node.exe` unless you kill  `processWatcher.exe` first .

Notice: 

>You don't have to put `processWatcher.exe` and `recovery.bat` in `E:\work` directory, however,  test shows that you have to put them in the same disk volume as `ffs-node-server.exe` and `node.exe`. 
>Again, you should modify the directory value in both the `processWacher.cpp` together with the `recovery.bat` if you want to confirm yourself.
