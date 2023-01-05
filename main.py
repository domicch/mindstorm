import uasyncio as asyncio
import hub


class MotorController:
    def __init__(self, port) -> None:
        self._port = port

    def forward(self):
        self._port.motor.run_at_speed(10)

    def backward(self):
        self._port.motor.run_at_speed(-10)

    def stop(self):
        self._port.motor.brake()


class UltrasonicController:
    def __init__(self, port) -> None:
        self._port = port
    
    def get_distance(self):
        return self._port.device.get()[0]


class MainController:
    def __init__(self) -> None:
        self._motor = MotorController(hub.port.A)
        self._ultrasonic = UltrasonicController(hub.port.F)
        
    async def work(self):
        while True:
            distance = self._ultrasonic.get_distance()

            if distance is not None and distance < 5:
                self._motor.stop()
            else:
                self._motor.forward()
            await asyncio.sleep_ms(100)


def set_global_exception():
    def handle_exception(loop, context):
        import sys
        sys.print_exception(context["exception"])
        sys.exit()
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(handle_exception)

async def main():
    set_global_exception()  # Debug aid
    main_controller = MainController()  # Constructor might create tasks
    task = asyncio.create_task(main_controller.work())  # Or you might do this
    await task  # Non-terminating method
try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()  # Clear retained state