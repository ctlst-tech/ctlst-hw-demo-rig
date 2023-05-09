cmake_minimum_required(VERSION 3.6)
set(ATOMIC_DEMO_PANEL_FSM_SRC
    g/demo_panel_fsm.h
    g/demo_panel_fsm_set_params.c
    g/demo_panel_fsm_spec.c
    g/demo_panel_fsm_interface.c
    demo_panel_fsm_exec.c
    )


add_library(atomic_demo_panel_fsm-static STATIC ${ATOMIC_DEMO_PANEL_FSM_SRC})

target_include_directories(atomic_demo_panel_fsm-static PRIVATE g)
target_include_directories(atomic_demo_panel_fsm-static PRIVATE ../../../../catpilot/c-atom/eswb/src/lib/include/public)
target_include_directories(atomic_demo_panel_fsm-static PRIVATE ../../../../catpilot/c-atom/function)
target_include_directories(atomic_demo_panel_fsm-static PUBLIC 
    ../../../../catpilot/c-atom/atomics/core/type/u32
    ../../../../catpilot/c-atom/atomics/core/type/bool
)
target_link_libraries(atomic_demo_panel_fsm-static PUBLIC bsp-static)
