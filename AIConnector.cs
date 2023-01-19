using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO.Ports;

public class AIConnector : MonoBehaviour
{

    SerialPort port;
    string com_name;
    int baud_rate;
    // Start is called before the first frame update
    void Start()
    {
        com_name= ""
        baud_rate= 19200
        port = new SerialPort(com_name, baud_rate)
        port.Open();
    }

    // Update is called once per frame
    void Update()
    {
        float[] recieved = new float[6];
        string[] received_str = port.ReadLine().Split(",");
        for(int i = 0; i < received_str.Length; i++)
        {
            received[i] = float.Parse(received_str[i]); 
        }
    }
}
