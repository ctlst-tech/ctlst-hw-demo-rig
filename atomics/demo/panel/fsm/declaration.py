from fspeclib import *

Function(
    name='demo.panel.fsm',
    title=LocalizedString(
        en='Buttons FSM'
    ),
    has_pre_exec_init_call=True,
    custom_cmakefile=True,
    parameters=[
        Parameter(
            name='initial',
            title='Initial',
            value_type='core.type.u32',
            tunable=False,
            default=0
        )
    ],
    inputs=[
        Input(
            name='button1',
            title='Input',
            value_type='core.type.bool',
        ),
        Input(
            name='button2',
            title='Input',
            value_type='core.type.bool',
        ),
        Input(
            name='button3',
            title='Input',
            value_type='core.type.bool',
        ),
        Input(
            name='button4',
            title='Input',
            value_type='core.type.bool',
        ),
    ],
    outputs=[
        Output(
            name='arm',
            title='Output',
            value_type='core.type.bool'
        ),
        Output(
            name='manual',
            title='Output',
            value_type='core.type.bool'
        ),
        Output(
            name='angrates',
            title='Output',
            value_type='core.type.bool'
        ),
        Output(
            name='special',
            title='Output',
            value_type='core.type.bool'
        ),
        Output(
            name='status',
            title='Output',
            value_type='core.type.bool'
        ),
        Output(
            name='enable_check_indication',
            title='Output',
            value_type='core.type.bool'
        ),
    ],
    state=[
        Variable(
            name='state',
            title='State',
            value_type='core.type.bool'
        ),
        Variable(
            name='enable_check_indication',
            title='State',
            value_type='core.type.bool'
        ),
    ],
    parameter_constraints=[]
)
