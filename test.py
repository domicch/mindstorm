import hub
import uasyncio


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

async def work():
    hub.sound.beep()

    hub.display.show(blinking_frames,
        clear=False,
        delay=round(1000 / 8),
        loop=True,
        fade=1)


async def main():
    print(uasyncio.__version__)
    await work()


uasyncio.run(main())

print("done")
