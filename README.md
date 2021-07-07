# metrics
Metrics is a lightweight, configurable system metrics broker.

# Description

## Device Type Classes

**Device Type Classes** are defined for each different type of device that one might want to make available for metrics data collection. All of these classes will indirectly implement the operations of the **Device Type Interface** which defines all of the operations that a Device Type Class must implement. They will do so, however, by extending a base class that provides core functionality shared between implementations of the Device Type Interface.

#### Device Type Interface (devicetypeinterface.py)
The device type interface specifies all of the operations that a Device Type Class must implement. These operations include initialization, collectible stats, etc.

#### Device Type Base Class (devicetypebaseclass.py)
This class is a base class that acts as a basic implementation of the Device Type Interface. This is included in order to provide basic, shared functionality that, while overridable, can be used across all Device Type Classes.

#### Device Type Classes
These classes are meant to extend the Device Type Base Class by overriding the implementations in the Device Type Base class.