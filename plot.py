import matplotlib.pyplot as plt
import numpy as np

# Plot for UDP Throughput
fig, ax = plt.subplots()
ax.set_ylim((0, 5.0))
ax.set_ylabel('Throughput (Gbps)')
ax.set_xlabel('Number of hops through network')
ax.set_title('Simulated Throughput of UDP Packets')
# Data
x_labels = ['1', '2', '3', '4']
throughput = [
    [3.80, 3.04, 2.64, 2.37], # flow-enabled
    [2.44, 2.31, 2.22, 2.39], # flow-disabled
]
x = np.arange(len(x_labels))
ax.set_xticks(x, x_labels)
bar_width = 0.35
rects1 = ax.bar(x-bar_width/2, throughput[0], width=bar_width, color='orange', label='flow-enabled')
rects2 = ax.bar(x+bar_width/2, throughput[1], width=bar_width, color='blue',   label='flow-disabled')
ax.legend()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
plt.savefig('plots_laptop/UDP_throughput.png')

# Plot for TCP Throughput
fig, ax = plt.subplots()
ax.set_ylim((0, 50.0))
ax.set_ylabel('Throughput (Gbps)')
ax.set_xlabel('Number of hops through network')
ax.set_title('Simulated Throughput of TCP Packets with Flow Entries')
# Data
x_labels = ['1', '2', '3', '4']
throughput = [
    [45.84, 41.84, 40.64, 39.56]
]
x = np.arange(len(x_labels))
ax.set_xticks(x, x_labels)
bar_width = 0.35
rects1 = ax.bar(x, throughput[0], width=bar_width, color='orange', label='flow-enabled')
ax.bar_label(rects1, padding=3)
plt.savefig('plots_laptop/TCP_throughput_flow_enabled.png')

# Plot for TCP Throughput
fig, ax = plt.subplots()
ax.set_ylim((0, 8.0))
ax.set_ylabel('Throughput (Mbps)')
ax.set_xlabel('Number of hops through network')
ax.set_title('Simulated Throughput of TCP Packets without Flow Entries')
# Data
x_labels = ['1', '2', '3', '4']
throughput = [
    [6.57, 3.13, 2.19, 1.59]
]
x = np.arange(len(x_labels))
ax.set_xticks(x, x_labels)
bar_width = 0.35
rects1 = ax.bar(x, throughput[0], width=bar_width, color='orange')
ax.bar_label(rects1, padding=3)
plt.savefig('plots_laptop/TCP_throughput_flow_disabled.png')


# Plot for ICMP round-trip latency in flow-enabled controller
fig, ax = plt.subplots()
ax.set_ylim((0, 0.40))
ax.set_ylabel('Latency/Jitter (milliseconds)')
ax.set_xlabel('Number of hops through network')
ax.set_title('Round-trip Latency of ICMP Echo Requests with Flows Entries')
# Data
x_labels = ['1', '2', '3', '4']
throughput = [
    [0.116, 0.176, 0.236, 0.240],
    [0.059, 0.177, 0.339, 0.336]
]
x = np.arange(len(x_labels))
ax.set_xticks(x, x_labels)
rects1 = ax.bar(x-bar_width/2, throughput[0], width=bar_width, color='black', label='latency')
rects2 = ax.bar(x+bar_width/2, throughput[1], width=bar_width, color='grey', label='jitter')
ax.legend(loc='upper left')
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
plt.savefig('plots_laptop/ICMP_latency_flow_enabled.png')

# Plot for ICMP round-trip latency in flow-disabled controller
fig, ax = plt.subplots()
ax.set_ylim((0, 36))
ax.set_ylabel('Latency/Jitter (milliseconds)')
ax.set_xlabel('Number of hops through network')
ax.set_title('Round-trip Latency of ICMP Echo Requests without Flow Entries')
# Data
x_labels = ['1', '2', '3', '4']
throughput = [
    [7.42, 13.19, 19.08, 29.20],
    [2.09, 4.76, 7.27, 12.21]
]
x = np.arange(len(x_labels))
ax.set_xticks(x, x_labels)
rects1 = ax.bar(x-bar_width/2, throughput[0], width=bar_width, color='black', label='latency')
rects2 = ax.bar(x+bar_width/2, throughput[1], width=bar_width, color='grey', label='jitter')
ax.legend(loc='upper left')
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
plt.savefig('plots_laptop/ICMP_latency_flow_disabled.png')