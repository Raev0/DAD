using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Diagnostics;
using System.Windows.Forms;


namespace processWatcher
{
    class Program
    {
        static void Main(string[] args)
        {
            service svs = new service();
            svs.Start();
            Console.WriteLine("这个窗口是个保证node server不被停掉的魔法程序，请不要动");
            while (true)
            {
                //running
            }

        }

    }

    class service 
    {
        static System.Timers.Timer timerGet = new System.Timers.Timer();
        public Process[] plist = Process.GetProcesses();
        public static String[] _processName;   // it is extremely import to declare a "static " member . all the value would not remain among functions' calls
        readonly String OBJECTPATH = "E:\\work\\recover.bat";//maybe it could be read from a text file.

        public service()
        {
            plist = Process.GetProcesses();
            _processName = new String[plist.Length];
            for (int i = 0; i < plist.Length; i++)
            {
                _processName[i] = plist[i].ProcessName;
            }
        }

        // override the service paremeters

        public void Start()
        {
            timerGet.Enabled = true;
            timerGet.Interval = 1000;
            timerGet.Elapsed += new System.Timers.ElapsedEventHandler(OnTimedEvent);
        }

        public void OnTimedEvent(object sender, System.Timers.ElapsedEventArgs e)
        {
    
            try
            {
              
                new service();
                bool crashed = !(_processName.Contains("ffs-node-server") && _processName.Contains("node"));

                if (crashed)
                {
                    System.Diagnostics.Process newP = new System.Diagnostics.Process();
                    newP.StartInfo.FileName = OBJECTPATH;
                    newP.Start();

                }

            }
            catch (Exception ex)
            {
                MessageBox.Show("错误:" + ex);
            }
            // 定时器响应函数
        }
        public void OnStop()
        {
            timerGet.Enabled = false;

        }
    }



}