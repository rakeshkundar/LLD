from observable.observable_interface import ObservableInterface
from observable.iphone_observable import IphoneObservable
from observer.observer_interface import ObserverInterface
from observer.email_observer import EmailObserver
from observer.mobile_observer import MobileObserver

if __name__ == '__main__':
    iphone_observable: ObservableInterface = IphoneObservable([], 0)
    mobile_observer: ObserverInterface = MobileObserver(iphone_observable)
    email_observer: ObserverInterface = EmailObserver(iphone_observable)

    # Registering observer to observable
    iphone_observable.register(mobile_observer)
    iphone_observable.register(email_observer)

    iphone_observable.increase_stock(10)
    # Unregistering email observer from iphone observable
    iphone_observable.unregister(email_observer)

    iphone_observable.decrease_stock(10)

    iphone_observable.increase_stock(10)
    iphone_observable.increase_stock(100)

