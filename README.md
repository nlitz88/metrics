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