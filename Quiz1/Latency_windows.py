import subprocess
import operator


ip_region_ip = {"us-east-1":"23.23.255.255",
                "us-west-1":"13.56.63.251",
                "eu-west-1":"34.240.0.253",
                "ap-northeast-1":"13.112.63.251",
                "us-west-2":"34.208.63.251",
                "ap-northeast-2":"13.124.63.251",
                "eu-central-1":"18.194.0.252",
                "ap-southeast-1":"13.228.0.251",
                "eu-west-2":"35.176.0.252",
                "us-gov-west-1":"52.61.0.254",
                "ap-southeast-2":"13.54.63.252",
                "us-east-2":"13.58.0.253",
                "ca-central-1":"35.182.0.251",
                "ap-south-1":"13.126.0.252",
                "sa-east-1":"18.231.0.252"
    }

ip_region_latency = {}

for region,ip in ip_region_ip.items():
    ping = subprocess.Popen(
            ["ping","-n","3",ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
    out, error = ping.communicate()
    out = str(out)
    out=out.split("\\r\\n")
    for ele in out:
        if "Average" in ele:
            avgline = (ele.split(',')[2]).split('=')[1]
            
            avgline = avgline.replace('ms','')
            
            ip_region_latency[region]=int(avgline)
            
            
            
for region, latency in sorted(ip_region_latency.items(), key=operator.itemgetter(1)):
    print(region + " [" + ip_region_ip[region] + "] - " + str(ip_region_latency[region]) + "ms")


