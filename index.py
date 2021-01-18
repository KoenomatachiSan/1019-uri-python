SECOND = int(input("SECOND:"));

MINUT = int(SECOND/60);
SECOND -= MINUT*60;
HOUR = int(MINUT/60);
MINUT -= HOUR*60;

print(repr(HOUR)+":"+repr(MINUT)+":"+repr(SECOND))