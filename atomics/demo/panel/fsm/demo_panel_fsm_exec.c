#include "demo_panel_fsm.h"
#include "demo_panel_fsm_proto.h"

fspec_rv_t demo_panel_fsm_pre_exec_init(const demo_panel_fsm_params_t *p,
                                        demo_panel_fsm_state_t *state) {
    state->state = DISARM;
    state->enable_check_indication = FALSE;
    return fspec_rv_ok;
}

void demo_panel_fsm_exec(const demo_panel_fsm_inputs_t *i,
                         demo_panel_fsm_outputs_t *o,
                         const demo_panel_fsm_params_t *p,
                         demo_panel_fsm_state_t *state) {
    if (i->button4) {
        state->state = DISARM;
        state->enable_check_indication = TRUE;
    } else {
        state->enable_check_indication = FALSE;
        if (i->button3) {
            state->state = MANUAL;
        } else if (i->button2) {
            state->state = ANGRATES;
        } else if (i->button1) {
            state->state = SPECIAL;
        }
    }
    if (state->state == DISARM) {
        o->arm = FALSE;
        o->manual = FALSE;
        o->angrates = FALSE;
        o->special = FALSE;
    } else {
        o->arm = TRUE;
        if (state->state == MANUAL) {
            o->manual = TRUE;
            o->angrates = FALSE;
            o->special = FALSE;
        } else if (state->state == ANGRATES) {
            o->manual = FALSE;
            o->angrates = TRUE;
            o->special = FALSE;
        } else if (state->state == SPECIAL) {
            o->manual = FALSE;
            o->angrates = FALSE;
            o->special = TRUE;
        }
    }
    o->enable_check_indication = state->enable_check_indication;
    return;
}
