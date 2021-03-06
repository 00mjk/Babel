// 
// File:          decaf_Services_Impl.hxx
// Symbol:        decaf.Services-v0.8.2
// Symbol Type:   class
// Babel Version: 2.0.0 (Revision: 7399M trunk)
// Description:   Server-side implementation for decaf.Services
// 
// WARNING: Automatically generated; only changes within splicers preserved
// 
// 

#ifndef included_decaf_Services_Impl_hxx
#define included_decaf_Services_Impl_hxx

#ifndef included_sidl_cxx_hxx
#include "sidl_cxx.hxx"
#endif
#ifndef included_decaf_Services_IOR_h
#include "decaf_Services_IOR.h"
#endif
#ifndef included_decaf_Services_hxx
#include "decaf_Services.hxx"
#endif
#ifndef included_gov_cca_AbstractFramework_hxx
#include "gov_cca_AbstractFramework.hxx"
#endif
#ifndef included_gov_cca_CCAException_hxx
#include "gov_cca_CCAException.hxx"
#endif
#ifndef included_gov_cca_ComponentID_hxx
#include "gov_cca_ComponentID.hxx"
#endif
#ifndef included_gov_cca_ComponentRelease_hxx
#include "gov_cca_ComponentRelease.hxx"
#endif
#ifndef included_gov_cca_Port_hxx
#include "gov_cca_Port.hxx"
#endif
#ifndef included_gov_cca_Services_hxx
#include "gov_cca_Services.hxx"
#endif
#ifndef included_gov_cca_TypeMap_hxx
#include "gov_cca_TypeMap.hxx"
#endif
#ifndef included_gov_cca_ports_ConnectionEventListener_hxx
#include "gov_cca_ports_ConnectionEventListener.hxx"
#endif
#ifndef included_gov_cca_ports_ConnectionEventService_hxx
#include "gov_cca_ports_ConnectionEventService.hxx"
#endif
#ifndef included_gov_cca_ports_EventType_hxx
#include "gov_cca_ports_EventType.hxx"
#endif
#ifndef included_gov_cca_ports_ServiceProvider_hxx
#include "gov_cca_ports_ServiceProvider.hxx"
#endif
#ifndef included_gov_cca_ports_ServiceRegistry_hxx
#include "gov_cca_ports_ServiceRegistry.hxx"
#endif
#ifndef included_sidl_BaseClass_hxx
#include "sidl_BaseClass.hxx"
#endif
#ifndef included_sidl_BaseInterface_hxx
#include "sidl_BaseInterface.hxx"
#endif
#ifndef included_sidl_ClassInfo_hxx
#include "sidl_ClassInfo.hxx"
#endif
#ifndef included_sidl_RuntimeException_hxx
#include "sidl_RuntimeException.hxx"
#endif


// DO-NOT-DELETE splicer.begin(decaf.Services._hincludes)
#include <map>
#include <list>
#include <utility>  // need pair<,>
// DO-NOT-DELETE splicer.end(decaf.Services._hincludes)

namespace decaf { 

  /**
   * Symbol "decaf.Services" (version 0.8.2)
   */
  class Services_impl : public virtual ::decaf::Services 
  // DO-NOT-DELETE splicer.begin(decaf.Services._inherits)
  // Put additional inheritance here...
  // DO-NOT-DELETE splicer.end(decaf.Services._inherits)

  {

  // All data marked protected will be accessable by 
  // descendant Impl classes
  protected:

    bool _wrapped;

    // DO-NOT-DELETE splicer.begin(decaf.Services._implementation)
    typedef std::map<std::string, std::pair<gov::cca::Port, gov::cca::TypeMap> > portMap_t;
    portMap_t d_providesPort;
    portMap_t d_usesPort;
    gov::cca::ComponentID d_componentID;    
    gov::cca::TypeMap d_instanceProperties;
    gov::cca::AbstractFramework d_fwk;
    ::std::map< ::std::string , ::std::string > d_portType;
    typedef std::list<gov::cca::ports::ConnectionEventListener> listenerList_t;
    typedef std::map< gov::cca::ports::EventType, listenerList_t > listeners_t;
    listeners_t d_listeners;
    bool d_is_alias; // true iff services object is bound to framework, not a real component
    // DO-NOT-DELETE splicer.end(decaf.Services._implementation)

  public:
    // default constructor, used for data wrapping(required)
    Services_impl();
    // sidl constructor (required)
    // Note: alternate Skel constructor doesn't call addref()
    // (fixes bug #275)
      Services_impl( struct decaf_Services__object * ior ) : StubBase(ior,true),
        
      ::gov::cca::Services((ior==NULL) ? NULL : &((*ior).d_gov_cca_services)),
      ::gov::cca::Port((ior==NULL) ? NULL : &((*ior).d_gov_cca_port)),
      ::gov::cca::ports::ConnectionEventService((ior==NULL) ? NULL : &((
        *ior).d_gov_cca_ports_connectioneventservice)),
    ::gov::cca::ports::ServiceRegistry((ior==NULL) ? NULL : &((
      *ior).d_gov_cca_ports_serviceregistry)) , _wrapped(false) {
      ior->d_data = this;
      _ctor();
    }


    // user defined construction
    void _ctor();

    // virtual destructor (required)
    virtual ~Services_impl() { _dtor(); }

    // user defined destruction
    void _dtor();

    // true if this object was created by a user newing the impl
    inline bool _isWrapped() {return _wrapped;}

    // static class initializer
    static void _load();

  public:

    /**
     * user defined non-static method.
     */
    void
    bindPort_impl (
      /* in */const ::std::string& portName,
      /* in */::gov::cca::Port& port
    )
    ;

    /**
     * user defined non-static method.
     */
    ::gov::cca::Port
    getProvidesPort_impl (
      /* in */const ::std::string& name
    )
    ;

    /**
     * user defined non-static method.
     */
    void
    initialize_impl (
      /* in */::gov::cca::AbstractFramework& fwk,
      /* in */::gov::cca::ComponentID& componentID,
      /* in */::gov::cca::TypeMap& properties,
      /* in */bool is_alias
    )
    ;

    /**
     * user defined non-static method.
     */
    ::gov::cca::TypeMap
    getInstanceProperties_impl() ;
    /**
     * user defined non-static method.
     */
    void
    setInstanceProperties_impl (
      /* in */::gov::cca::TypeMap& properties
    )
    ;

    /**
     * user defined non-static method.
     */
    void
    setPortProperties_impl (
      /* in */const ::std::string& portName,
      /* in */::gov::cca::TypeMap& properties
    )
    ;

    /**
     * user defined non-static method.
     */
    ::sidl::array< ::std::string>
    getProvidedPortNames_impl() ;
    /**
     * user defined non-static method.
     */
    ::sidl::array< ::std::string>
    getUsedPortNames_impl() ;
    /**
     * user defined non-static method.
     */
    void
    notifyConnectionEvent_impl (
      /* in */const ::std::string& portName,
      /* in */::gov::cca::ports::EventType event
    )
    ;


    /**
     *  
     * Fetch a previously registered Port (defined by either 
     * addProvidePort or (more typically) registerUsesPort).  
     * @return Will return the Port (possibly waiting forever while
     * attempting to acquire it) or throw an exception. Does not return
     * NULL, even in the case where no connection has been made. 
     * If a Port is returned,
     * there is then a contract that the port will remain valid for use
     * by the caller until the port is released via releasePort(), or a 
     * Disconnect Event is successfully dispatched to the caller,
     * or a runtime exception (such as network failure) occurs during 
     * invocation of some function in the Port. 
     * <p>
     * Subtle interpretation: If the Component is not listening for
     * Disconnect events, then the framework has no clean way to
     * break the connection until after the component calls releasePort.
     * </p>
     * <p>The framework may go through some machinations to obtain
     * the port, possibly involving an interactive user or network 
     * queries, before giving up and throwing an exception.
     * </p>
     * 
     * @param portName The previously registered or provide port which
     * the component now wants to use.
     * @exception CCAException with the following types: NotConnected, PortNotDefined, 
     * NetworkError, OutOfMemory.
     */
    ::gov::cca::Port
    getPort_impl (
      /* in */const ::std::string& portName
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;


    /**
     *  
     * Get a previously registered Port (defined by
     * either addProvide or registerUses) and return that
     * Port if it is available immediately (already connected
     * without further connection machinations).
     * There is an contract that the
     * port will remain valid per the description of getPort.
     * @return The named port, if it exists and is connected or self-provided,
     * or NULL if it is registered and is not yet connected. Does not
     * return if the Port is neither registered nor provided, but rather
     * throws an exception.
     * @param portName registered or provided port that
     * the component now wants to use.
     * @exception CCAException with the following types: PortNotDefined, OutOfMemory.
     */
    ::gov::cca::Port
    getPortNonblocking_impl (
      /* in */const ::std::string& portName
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;


    /**
     *  
     * Notifies the framework that this component is finished 
     * using the previously fetched Port that is named.     
     * The releasePort() method calls should be paired with 
     * getPort() method calls; however, an extra call to releasePort()
     * for the same name may (is not required to) generate an exception.
     * Calls to release ports which are not defined or have never be fetched
     * with one of the getPort functions generate exceptions.
     * @param portName The name of a port.
     * @exception CCAException with the following types: PortNotDefined, PortNotInUse.
     */
    void
    releasePort_impl (
      /* in */const ::std::string& portName
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;


    /**
     * Creates a TypeMap, potentially to be used in subsequent
     * calls to describe a Port.  Initially, this map is empty.
     */
    ::gov::cca::TypeMap
    createTypeMap_impl() // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;

    /**
     *  
     * Register a request for a Port that will be retrieved subsequently 
     * with a call to getPort().
     * @param portName A string uniquely describing this port.  This string
     * must be unique for this component, over both uses and provides ports.
     * @param type A string desribing the type of this port.
     * @param properties A TypeMap describing optional properties
     * associated with this port. This can be a null pointer, which
     * indicates an empty list of properties.  Properties may be
     * obtained from createTypeMap or any other source.  The properties
     * be copied into the framework, and subsequent changes to the
     * properties object will have no effect on the properties
     * associated with this port.
     * In these properties, all frameworks recognize at least the
     * following keys and values in implementing registerUsesPort:
     * <pre>
     * key:              standard values (in string form)     default
     * "MAX_CONNECTIONS" any nonnegative integer, "unlimited".   1
     * "MIN_CONNECTIONS" any integer > 0.                        0
     * "ABLE_TO_PROXY"   "true", "false"                      "false"
     * </pre>
     * The component is not expected to work if the framework
     * has not satisfied the connection requirements.
     * The framework is allowed to return an error if it
     * is incapable of meeting the connection requirements,
     * e.g. it does not implement multiple uses ports.
     * The caller of registerUsesPort is not obligated to define
     * these properties. If left undefined, the default listed above is
     * assumed.
     * @exception CCAException with the following types: PortAlreadyDefined, OutOfMemory.
     */
    void
    registerUsesPort_impl (
      /* in */const ::std::string& portName,
      /* in */const ::std::string& type,
      /* in */::gov::cca::TypeMap& properties
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;


    /**
     *  
     * Notify the framework that a Port, previously registered by this
     * component but currently not in use, is no longer desired. 
     * Unregistering a port that is currently 
     * in use (i.e. an unreleased getPort() being outstanding) 
     * is an error.
     * @param portName The name of a registered Port.
     * @exception CCAException with the following types: UsesPortNotReleased, PortNotDefined.
     */
    void
    unregisterUsesPort_impl (
      /* in */const ::std::string& portName
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;


    /**
     *  
     * Exposes a Port from this component to the framework.  
     * This Port is now available for the framework to connect 
     * to other components. 
     * @param inPort An abstract interface (tagged with CCA-ness
     * by inheriting from gov.cca.Port) the framework will
     * make available to other components.
     * 
     * @param portName string uniquely describing this port.  This string
     * must be unique for this component, over both uses and provides ports.
     * 
     * @param type string describing the type (class) of this port.
     * 
     * @param properties A TypeMap describing optional properties
     * associated with this port. This can be a null pointer, which
     * indicates an empty list of properties.  Properties may be
     * obtained from createTypeMap or any other source.  The properties
     * be copied into the framework, and subsequent changes to the
     * properties object will have no effect on the properties
     * associated with this port.
     * In these properties, all frameworks recognize at least the
     * following keys and values in implementing registerUsesPort:
     * <pre>
     * key:              standard values (in string form)     default
     * "MAX_CONNECTIONS" any nonnegative integer, "unlimited".   1
     * "MIN_CONNECTIONS" any integer > 0.                        0
     * "ABLE_TO_PROXY"   "true", "false"                      "false"
     * </pre>
     * The component is not expected to work if the framework
     * has not satisfied the connection requirements.
     * The framework is allowed to return an error if it
     * is incapable of meeting the connection requirements,
     * e.g. it does not implement multiple uses ports.
     * The caller of addProvidesPort is not obligated to define
     * these properties. If left undefined, the default listed above is
     * assumed.
     * @exception CCAException with the following types: PortAlreadyDefined, OutOfMemory.
     */
    void
    addProvidesPort_impl (
      /* in */::gov::cca::Port& inPort,
      /* in */const ::std::string& portName,
      /* in */const ::std::string& type,
      /* in */::gov::cca::TypeMap& properties
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;


    /**
     *  Returns the complete list of the properties for a Port.  This
     * includes the properties defined when the port was registered
     * (these properties can be modified by the framework), two special
     * properties "cca.portName" and "cca.portType", and any other
     * properties that the framework wishes to disclose to the component.
     * The framework may also choose to provide only the subset of input
     * properties (i.e. from addProvidesPort/registerUsesPort) that it
     * will honor.      
     */
    ::gov::cca::TypeMap
    getPortProperties_impl (
      /* in */const ::std::string& name
    )
    ;


    /**
     *  Notifies the framework that a previously exposed Port is no longer 
     * available for use. The Port being removed must exist
     * until this call returns, or a CCAException may occur.
     * @param portName The name of a provided Port.
     * @exception PortNotDefined. In general, the framework will not dictate 
     * when the component chooses to stop offering services.
     */
    void
    removeProvidesPort_impl (
      /* in */const ::std::string& portName
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;


    /**
     *  
     * Get a reference to the component to which this 
     * Services object belongs. 
     */
    ::gov::cca::ComponentID
    getComponentID_impl() ;

    /**
     *  Obtain a callback for component destruction.
     * @param callBack an object that implements the ComponentRelease
     * interface that will be called when the component is to be destroyed.
     * 
     * Register a callback to be executed when the component is going
     * to be destroyed.  During this callback, the Services object passed
     * through setServices will still be valid, but after all such
     * callbacks are made for a specific component, subsequent usage
     * of the Services object is not allowed/is undefined.
     */
    void
    registerForRelease_impl (
      /* in */::gov::cca::ComponentRelease& callBack
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;


    /**
     *  
     * Sign up to be told about connection activity.
     * connectionEventType must be one of the integer 
     * values defined iN ConnectionEvent. 
     */
    void
    addConnectionEventListener_impl (
      /* in */::gov::cca::ports::EventType et,
      /* in */::gov::cca::ports::ConnectionEventListener& cel
    )
    ;


    /**
     *  
     * Ignore future ConnectionEvents of the given type.
     * connectionEventType must be one of the integer values 
     * defined in ConnectionEvent. 
     */
    void
    removeConnectionEventListener_impl (
      /* in */::gov::cca::ports::EventType et,
      /* in */::gov::cca::ports::ConnectionEventListener& cel
    )
    ;


    /**
     * Add a ServiceProvider that can be asked to produce service Port's
     * for other components to use subsequently.
     * True means success. False means that for some reason, the
     * provider isn't going to function. Possibly another server is doing
     * the job.
     */
    bool
    addService_impl (
      /* in */const ::std::string& serviceType,
      /* in */::gov::cca::ports::ServiceProvider& portProvider
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;


    /**
     *  Add a "reusable" service gov.cca.Port for other components to use 
     * subsequently.
     */
    bool
    addSingletonService_impl (
      /* in */const ::std::string& serviceType,
      /* in */::gov::cca::Port& server
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;


    /**
     *  Inform the framework that this service Port is no longer to
     * be used, subsequent to this call. 
     */
    void
    removeService_impl (
      /* in */const ::std::string& serviceType
    )
    // throws:
    //    ::gov::cca::CCAException
    //    ::sidl::RuntimeException
    ;

  };  // end class Services_impl

} // end namespace decaf

// DO-NOT-DELETE splicer.begin(decaf.Services._hmisc)
// Put miscellaneous things here...
// DO-NOT-DELETE splicer.end(decaf.Services._hmisc)

#endif
