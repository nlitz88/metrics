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

#### Publisher/Producer interface
This interface would define operations like publish_data that would essentially receive that generic python dictionary with a devices data, transform it to whatever form is required (JSON), and then publish it to whichever service/server it is built for.


TODO: there should be a separate python module (not interface) that is responsible for taking the data and making it available via a REST API. This could be like metricsserver or something.
Anyways, the plan is to cache the data in redis, and then that server would basically be pulling data from redis upon request. Could also implement custom endpoints to make direct calls to get values directlyl raqther than through redis.