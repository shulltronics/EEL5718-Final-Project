import matplotlib.pyplot as plt
import numpy as np

# Plot for UDP Throughput
fig, ax = plt.subplots()
ax.set_ylim((0, 4.0))
ax.set_ylabel('Throughput (Gbps)')
ax.set_xlabel('Number of hops through network')
ax.set_title('Simulated Throughput of UDP Packets')
# Data
x_labels = ['1', '2', '3']
throughput = [
    [3.01, 2.71, 2.43], # flow-enabled
    [2.30, 2.27, 2.99], # flow-disabled
]
x = np.arange(len(x_labels))
ax.set_xticks(x, x_labels)
bar_width = 0.35
rects1 = ax.bar(x-bar_width/2, throughput[0], width=bar_width, color='orange', label='flow-enabled')
rects2 = ax.bar(x+bar_width/2, throughput[1], width=bar_width, color='blue',   label='flow-disabled')
ax.legend()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
plt.savefig('plots/UDP_throughput.png')

# Plot for TCP Throughput
fig, ax = plt.subplots()
ax.set_ylim((0, 42.0))
ax.set_ylabel('Throughput (Gbps)')
ax.set_xlabel('Number of hops through network')
ax.set_title('Simulated Throughput of TCP Packets with Flow Entries')
# Data
x_labels = ['1', '2', '3']
throughput = [
    [35.2, 35.8, 32.4]
]
x = np.arange(len(x_labels))
ax.set_xticks(x, x_labels)
bar_width = 0.35
rects1 = ax.bar(x, throughput[0], width=bar_width, color='orange', label='flow-enabled')
ax.bar_label(rects1, padding=3)
plt.savefig('plots/TCP_throughput_flow_enabled.png')

# Plot for TCP Throughput
fig, ax = plt.subplots()
ax.set_ylim((0, 20.0))
ax.set_ylabel('Throughput (Mbps)')
ax.set_xlabel('Number of hops through network')
ax.set_title('Simulated Throughput of TCP Packets without Flow Entries')
# Data
x_labels = ['1', '2', '3']
throughput = [
    [15.1, 7.9, 5.4]
]
x = np.arange(len(x_labels))
ax.set_xticks(x, x_labels)
bar_width = 0.35
rects1 = ax.bar(x, throughput[0], width=bar_width, color='orange')
ax.bar_label(rects1, padding=3)
plt.savefig('plots/TCP_throughput_flow_disabled.png')


# Plot for ICMP round-trip latency in flow-enabled controller
fig, ax = plt.subplots()
ax.set_ylim((0, 60))
ax.set_ylabel('Latency/Jitter (microseconds)')
ax.set_xlabel('Number of hops through network')
ax.set_title('Round-trip Latency of ICMP Echo Requests with Flows Entries')
# Data
x_labels = ['1', '2', '3']
throughput = [
    [40, 43, 47],
    [14, 9, 7]
]
x = np.arange(len(x_labels))
ax.set_xticks(x, x_labels)
rects1 = ax.bar(x-bar_width/2, throughput[0], width=bar_width, color='black', label='latency')
rects2 = ax.bar(x+bar_width/2, throughput[1], width=bar_width, color='grey', label='jitter')
ax.legend()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
plt.savefig('plots/ICMP_latency_flow_enabled.png')

# Plot for ICMP round-trip latency in flow-enabled controller
fig, ax = plt.subplots()
ax.set_ylim((0, 6))
ax.set_ylabel('Latency/Jitter (milliseconds)')
ax.set_xlabel('Number of hops through network')
ax.set_title('Round-trip Latency of ICMP Echo Requests without Flow Entries')
# Data
x_labels = ['1', '2', '3']
throughput = [
    [1.96, 3.54, 4.82],
    [0.164, 0.445, 0.454]
]
x = np.arange(len(x_labels))
ax.set_xticks(x, x_labels)
rects1 = ax.bar(x-bar_width/2, throughput[0], width=bar_width, color='black', label='latency')
rects2 = ax.bar(x+bar_width/2, throughput[1], width=bar_width, color='grey', label='jitter')
ax.legend(loc='upper left')
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
plt.savefig('plots/ICMP_latency_flow_disabled.png')