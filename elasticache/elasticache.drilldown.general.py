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
        query='label_values(aws_ec_cpuutilization_average, environment)',
        type='query',
        includeAll=False,
        multi=False,
    )

Cluster = Template(
        name='cluster',
        label='Cluster',
        query='label_values(aws_ec_curr_items_average{environment="$environment"}, dimension_cache_cluster_id)',
        type='query',
        includeAll=False,
        multi=False,
        regex='/^(.*?)(-[\d]+)*$/'
    )

dashboard = Dashboard(
    title="SRE Elasticache Drilldowns",
    templating=Templating(list=[Environment, Cluster]),
    rows=[
        Row(panels=[
          Graph(
              title="Freeable Memory",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_freeable_memory_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=BYTES_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Bytes Used for Cache",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_bytes_used_for_cache_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=BYTES_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            )
        ]),
        Row(panels=[
            Graph(
              title="Swap Usage",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_swap_usage_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=BYTES_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Database Memory Usage",
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
        ]),
        Row(panels=[
            Graph(
              title="Freeable Memory",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_freeable_memory_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=BYTES_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Fragmentation Ratio",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_memory_fragmentation_ratio_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=PERCENT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Current Connections",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_curr_connections_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="New Connections",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_new_connections_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Cache Hits",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_cache_hits_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Cache Misses",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_cache_misses_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Redis SET Type Commands Latency (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_set_type_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format="µs"),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Redis GET Type Commands Latency (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_get_type_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
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
              title="Redis KEY Based Commands Latency (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_key_based_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format="µs"),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Redis SORTED SET Based Commands Latency (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_sorted_set_based_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
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
              title="Redis HASH Based Commands Latency (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_hash_based_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format="µs"),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Redis String Based Commands Latency (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_string_based_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
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
              title="Redis SET Based Commands Latency (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_set_based_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format="µs"),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Redis LIST Based Commands Latency (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_list_based_cmds_latency_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
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
              title="Redis SET Type Commands (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_set_type_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Redis GET Type Commands (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_get_type_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Redis KEY Based Commands (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_key_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Redis SORTED SET Based Commands (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_sorted_set_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Redis HASH Based Commands (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_hash_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Redis String Based Commands (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_string_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Redis SET Based Commands (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_set_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Redis LIST Based Commands (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_list_based_cmds_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Reclaimed Items (key expiration events)",
                dataSource=DATASOURCE,
                targets=[
                   Target(
                        expr='aws_ec_reclaimed_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Current Items",
                dataSource=DATASOURCE,
                targets=[
                   Target(
                        expr='aws_ec_curr_items_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Evicted Items",
                dataSource=DATASOURCE,
                targets=[
                   Target(
                        expr='aws_ec_evictions_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Host CPU Utilization",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_cpuutilization_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=PERCENT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Redis CPU Utilization",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_engine_cpuutilization_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=PERCENT_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Network Bytes In (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_network_bytes_in_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Network Bytes Out (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_network_bytes_out_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
        Row(panels=[
            Graph(
              title="Network Packets In (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_network_packets_in_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
            Graph(
              title="Network Packets Out (avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_network_packet_out_average{environment="${environment}", dimension_cache_cluster_id=~"${cluster}.*"}',
                        legendFormat="{{dimension_cache_cluster_id}}",
                        refId='A',
                    ),
                ],
                yAxes=YAxes(
                    YAxis(format=OPS_FORMAT),
                    YAxis(format=SHORT_FORMAT),
                ),
            ),
        ]),
    ],
).auto_panel_ids()