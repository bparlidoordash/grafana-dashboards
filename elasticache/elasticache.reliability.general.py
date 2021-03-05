from grafanalib.core import (
    Alert, AlertCondition, Dashboard, Graph, GaugePanel,
    GreaterThan, OP_AND, OPS_FORMAT, Row, RTYPE_SUM, SECONDS_FORMAT, 
    PERCENT_FORMAT, BYTES_FORMAT, PERCENT_UNIT_FORMAT,
    SHORT_FORMAT, single_y_axis, Target, Template, Templating, TimeRange, YAxes, YAxis
)

DATASOURCE="Chronosphere Prometheus"

Environment = Template(
        name='environment',
        label='Environment',
        query='label_values(aws_ec_cache_hits_average, environment)',
        type='query',
        includeAll=False,
        multi=False,
    )

Cluster = Template(
        name='cluster',
        label='Redis Cluster',
        query='label_values(aws_ec_curr_items_average{environment="$environment"}, dimension_cache_cluster_id)',
        type='query',
        includeAll=False,
        multi=False,
        regex='/^(.*?)(-[\d]+)*$/'
    )

dashboard = Dashboard(
    title="SRE Elasticache",
    templating=Templating(list=[Environment, Cluster]),
    rows=[
        Row(panels=[
          Graph(
              title="Redis Commands Ops(avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_set_type_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="set_type-{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                    Target(
                        expr='aws_ec_get_type_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="get-{{dimension_cache_cluster_id}}",
                        refId='B',
                    ),
                    Target(
                        expr='aws_ec_string_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="string-{{dimension_cache_cluster_id}}",
                        refId='C',
                    ),
                    Target(
                        expr='aws_ec_key_based_commands_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="key-{{dimension_cache_cluster_id}}",
                        refId='D',
                    ),
                    Target(
                        expr='aws_ec_sorted_set_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="sorted_set-{{dimension_cache_cluster_id}}",
                        refId='E',
                    ),
                    Target(
                        expr='aws_ec_set_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="set_based-{{dimension_cache_cluster_id}}",
                        refId='F',
                    ),
                    Target(
                        expr='aws_ec_hash_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="hash-{{dimension_cache_cluster_id}}",
                        refId='G',
                    ),
                    Target(
                        expr='aws_ec_list_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="list-{{dimension_cache_cluster_id}}",
                        refId='H',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format="µs"),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Redis Commands Latency (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_set_type_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="set_type-{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                    Target(
                        expr='aws_ec_get_type_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="get-{{dimension_cache_cluster_id}}",
                        refId='B',
                    ),
                    Target(
                        expr='aws_ec_string_based_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="string-{{dimension_cache_cluster_id}}",
                        refId='C',
                    ),
                    Target(
                        expr='aws_ec_key_type_based_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="key-{{dimension_cache_cluster_id}}",
                        refId='D',
                    ),
                    Target(
                        expr='aws_ec_sorted_set_based_latency_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="sorted_set-{{dimension_cache_cluster_id}}",
                        refId='E',
                    ),
                    Target(
                        expr='aws_ec_set_based_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="set_based-{{dimension_cache_cluster_id}}",
                        refId='F',
                    ),
                    Target(
                        expr='aws_ec_hash_based_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="hash-{{dimension_cache_cluster_id}}",
                        refId='G',
                    ),
                    Target(
                        expr='aws_ec_list_based_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="list-{{dimension_cache_cluster_id}}",
                        refId='H',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format="µs"),
                    YAxis(format=SHORT_FORMAT),
                ),
            )
        ]),
        Row(panels=[
            Graph(
              title="Redis Database Memory Usage (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_database_memory_usage_percentage_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=PERCENT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            GaugePanel(
              title="Redis Swap (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_swap_usage_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
            ),
        ]),
        Row(panels=[
          Graph(
              title="Memory Fragmentation Ratio (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_memory_fragmentation_ratio_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    )
                ],
                yAxes=YAxes(
                    YAxis(format=SHORT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
          Graph(
              title="Current Connections (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_curr_connections_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    )
                ],
                yAxes=YAxes(
                    YAxis(format=SHORT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="New Connections (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_new_connections_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    )
                ],
                yAxes=YAxes(
                    YAxis(format=SHORT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
          Graph(
              title="Hit Rate (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_cache_hit_rate_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    )
                ],
                yAxes=YAxes(
                    YAxis(format=PERCENT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Misses (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_cache_misses_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    )
                ],
                yAxes=YAxes(
                    YAxis(format=SHORT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
          Graph(
              title="Current Items Count (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_curr_items_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    )
                ],
                yAxes=YAxes(
                    YAxis(format=SHORT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Evictions (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_evictions_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    )
                ],
                yAxes=YAxes(
                    YAxis(format=SHORT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
    ],
).auto_panel_ids()