import hub
from runtime import VirtualMachine

blinking_animation = [
    "77077:00000:99099:99099:00000",
    "77077:00000:99099:99099:00000",
    "77077:00000:99099:99099:00000",
    "77077:00000:99099:99099:00000",
    "77077:00000:00000:77077:00000",
    "77077:00000:00000:00000:00000",
    "77077:00000:00000:88088:00000",
    "77077:00000:99099:99099:00000",
    "77077:00000:99099:99099:00000",
    "77077:00000:99099:99099:00000",
    "77077:00000:99099:99099:00000",
    "77077:00000:99099:99099:00000",
    "77077:00000:99099:99099:00000",
    "77077:00000:99099:99099:00000",
    "77077:00000:99099:99099:00000",
]
blinking_frames = [hub.Image(frame) for frame in blinking_animation]


async def on_start(vm, stack):
    print("This is the spot of your code")
    hub.sound.beep()
    


def setup(rpc, system, stop):
    vm = VirtualMachine(rpc, system, stop, "something_unique")
    vm.register_on_start("another_unique_string", on_start)
    vm.system.sound.beep()
    vm.system.display.show(blinking_frames,
        clear=False,
        delay=round(1000 / 8),
        loop=True,
        fade=1)
    return vm