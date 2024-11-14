#include "tweak_globals.h"

void SystemArena_Init(void* start, size_t size);
void SystemHeap_RunInits();

RECOMP_IMPORT(".", u32 hello());

void Schmiddys_Tweaks_Init(){
    recomp_printf("Schmiddy's Tweaks is Initializing... %d", hello());
}

RECOMP_PATCH void SystemHeap_Init(void* start, size_t size) {

    Schmiddys_Tweaks_Init();

    SystemArena_Init(start, size);
    SystemHeap_RunInits();
}


