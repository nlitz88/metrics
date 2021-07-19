# Potential Ideas
Just a document for me to rattle off some potential design changes that I might introduce in the future to either make metrics host a.) more configurable or b.) faster.

### Define Device_Metric Classes, rather than devices
The user cares about the data that they are collecting from devices, not the actual devices themselves. Therefore, it occurred to me that perhaps it would be more configurable (and just more practical) to define each metric that the user wants to collect, rather than the actual device.

I came to this conclusion for a number of reasons, but this particular example is what sparked my thinking:

Take a hard drive, for instance. A hard drive has multiple data points / metrics that I might want to collect. Temperature, amount of data written over some period, capacity, current utilization, etc. In the current model, I would define a hard drive device as an implementation of the device interface (extend the device base class), and it would follow that I would specify a list of metrics that I have created support for collecting. This means in my implementation's get_device_data method, I would have to write the code to grab each one of those specified data points and then return them all as a json object.

1. In the case of a hard drive, however, each one of those metrics might take a different amount of time to retrieve. Temperature takes a lot longer to get from hddtemp than current utilization from df. What if I need a very fast stream of data of the current utilization? If a device's metrics are all collected and published in one block, this could seriously bottleneck the collection of other data points that don't take very long to record.

2. Also in the scenario of a hard drive, I might only be interested in actually collecting/publishing a single one of those metrics. Thinking more broadly, what if you have a device with tens of attributes/collectible data points, but really only care about grabbing one of them? I don't want to force a user to have to publish more data to a particular service than absolutely necessary. Again, this should be in their control. It should be configurable.

Therefore, I'm starting to wonder if the notion of a "device" is really necessary. The only practical benefit to grouping metrics coming from the same device together is just for simplicity, but doesn't really seem practical. I think the only real tangible benefit to grouping metrics together for a device is if they're all retrieved using the same command (and that single command is rather slow). 

In this case, **maybe** it would be possible to specify a new type of "multi-metric" that collects a bunch of datapoints with a single command. Then, add support for getting data from this multi-metric (rather than using a command) in the metric class?

### Runner class Idea
OR, perhaps another method would be to define a new class called a **runner**. A runner would be a threaded process that is solely responsible for grabbing data. In this way, multiple **metric** instances can share the output of the same runner instance's data.

So, when users go to create a new metric, they have to implement a new instance of the **runner interface** which will contain the commands to extract the data that they need, as well as a new implementation of the **metric** implementation. A metric can therefore theoretically build it's result from the output of multiple runner threads, or more likely, multiple metrics can construct their data from a single runner instance.

Examples:
- For instance, if your GPU has a single command that outputs lots of power metrics at once, but takes a while to run, you could configure a single runner thread to run the command once and multiple metric instances to grab the data their data from the buffer of that single runner instance.


### How metric instances and runners will talk, general data flow / operation.
- Each runner instance runs in a thread, (will wrap this in a threaded_runner class of sorts), and this threaded_runner class will have a shared data buffer (will be a producer) that multiple other threads can read data from. (Consumers reading won't remove the data from the buffer's though).
- Each **metric** instance will one or multiple runners that it will talk to (specified in the config) and one or multiple publishers.
AGAIN, in this way, runners and publishers can be re-used by each metric.
A redis publisher can be