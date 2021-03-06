# metrics
Metrics is a lightweight, configurable system metrics broker.

# Description

## Device Classes

**Device Classes** are defined for each different type of device that one might want to make available for metrics data collection. All of these classes will indirectly implement the operations of the **Device Interface** which defines all of the operations that a Device Class must implement. They will do so, however, by extending a base class that provides core functionality shared between implementations of the Device Interface.

#### Device Interface (deviceinterface.py)
The Device interface specifies all of the operations that a Device Class must implement. These operations include initialization, standard methods of retrieving data, etc.

#### Device Base Class (devicebaseclass.py)
This class is a base class that acts as a basic implementation of the Device Interface. This is included in order to provide basic, shared functionality that, while overridable, can be used across all Device Classes.

#### Device Classes
These classes are meant to extend the Device Base Class by overriding the implementations in the Device Base class as well as adding other custom operations as needed.


## Publisher Classes

**Publisher Classes** are defined for each different type of system that messages might want to be published to repeatedly. For instance, you might have a pubisher for mqtt, one for publishing values to a redis database, or maybe to mongo for long term storage.

#### Publisher/Producer Interface
This interface would define operations like publish_data that would essentially receive that generic python dictionary with a devices data, transform it to whatever form is required (JSON), and then publish it to whichever service/server it is built for.


TODO: there should be a separate python module (not interface) that is responsible for taking the data and making it available via a REST API. This could be like metricsserver or something.
Anyways, the plan is to cache the data in redis, and then that server would basically be pulling data from redis upon request. Could also implement custom endpoints to make direct calls to get values directlyl raqther than through redis.

# TODO: Detail the difference between the metrics host container, (redis, and metrics server). This is how the application will be split up.
# Multiple host instances can talk to the same redis instance, for instance.

<!-- ## Host Classes
**Host Classes** are defined for each different type of host that a publisher class might use to retrieve its data. This might be more appropriate in a situation where someone wants to utilize the publishing infrastructure of metrics without the default host class with all of its device collection methods. Hosts have a list of devices and publishers that they interact with.

Additionally, a more common implementation of this interface is having both local and remote host implementations. In this way, one instance of metrics can instantiate multiple hosts, grabbing data from a local host that connects to the docker socket and another host whose devices are in a virtual machine and must be queried via ssh. In this model, devices in the devices.yaml file would specify a host. Additionally, a hosts.yaml file would define hosts by hosttype and IP adddress (and potentially any other variant/types that might be created).

One machine would have one instance of metrics running (perhaps on the hypervisor, or a dockerhost vm) that spawns hosts in new threads (or just one thread, multiple connections, something like this) where they can then be used to get their respective device data.

#### Host Interface
This interface defines the operations that each host class must implement. If a class is a host, then it must be able to initialize a list of devices to get data from, publish device data to a list of publishers, etc. There may be more requirements as time moves along.

#### Host Base Class
This class will serve as the core of the **metrics** application. As the default host, it will initialize a list of device objects, make calls to those devices to retrieve their data, and then send data to each in a list of publishers. Again, the functionality of this class may vary significantly as development continues, but this is the general intention of this class as of right now. -->



# Question: Do I just want to rewrite what I have of this so far in GO just for the sake of learning it? Maybe...

# UPDATE: I decided to bag this project simply because I basically ended up designing the groundwork for...Telegraf. Unbeknownst to me, this was exactly what I was looking for and built just like what I was gearing up for. Though I would've liked to develop down this rabbit hole, I had to consider the practicality of using Telegraf and just how much more robust it already was.
