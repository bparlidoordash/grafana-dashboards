from grafanalib.core import (
    Alert, AlertCondition, Dashboard, Graph, GaugePanel,
    GreaterThan, OP_AND, OPS_FORMAT, Row, RTYPE_SUM, SECONDS_FORMAT, 
    PERCENT_FORMAT, BYTES_FORMAT, PERCENT_UNIT_FORMAT,
    SHORT_FORMAT, single_y_axis, Target, Template, Templating, TimeRange, YAxes, YAxis
)

DATASOURCE="Chronosphere Prometheus"

Region = Template(
        name='Region',
        label='Region',
        query='label_values(aws_ec_cache_hits_average,  region)',
        type='query',
        includeAll=True,
        multi=True,
    )

Cluster = Template(
        name='Cluster',
        label='Cluster',
        query='label_values(aws_ec_cache_hits_average{region=~"$Region"}, dimension_CacheClusterId)',
        type='query',
        includeAll=True,
        multi=True,
    )

dashboard = Dashboard(
    title="Elasticache Reliability",
    templating=Templating(list=[Region, Cluster]),
    rows=[
        Row(panels=[
          Graph(
              title="Redis Commands Ops(avg)",
                dataSource=DATASOURCE,
                targets=[
                    Target(
                        expr='aws_ec_set_type_cmds_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="set_type-{{dimension_CacheClusterId}}",
                        refId='A',
                    ),
                    Target(
                        expr='aws_ec_get_type_cmds_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="get-{{dimension_CacheClusterId}}",
                        refId='B',
                    ),
                    Target(
                        expr='aws_ec_string_based_cmds_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="string-{{dimension_CacheClusterId}}",
                        refId='C',
                    ),
                    Target(
                        expr='aws_ec_key_type_based_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="key-{{dimension_CacheClusterId}}",
                        refId='D',
                    ),
                    Target(
                        expr='aws_ec_sorted_set_based_cmds_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="sorted_set-{{dimension_CacheClusterId}}",
                        refId='E',
                    ),
                    Target(
                        expr='aws_ec_set_based_cmds_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="set_based-{{dimension_CacheClusterId}}",
                        refId='F',
                    ),
                    Target(
                        expr='aws_ec_hash_based_cmds_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="hash-{{dimension_CacheClusterId}}",
                        refId='G',
                    ),
                    Target(
                        expr='aws_ec_list_based_cmds_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="list-{{dimension_CacheClusterId}}",
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
                        expr='aws_ec_set_type_cmds_latency_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="set_type-{{dimension_CacheClusterId}}",
                        refId='A',
                    ),
                    Target(
                        expr='aws_ec_get_type_cmds_latency_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="get-{{dimension_CacheClusterId}}",
                        refId='B',
                    ),
                    Target(
                        expr='aws_ec_string_based_cmds_latency_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="string-{{dimension_CacheClusterId}}",
                        refId='C',
                    ),
                    Target(
                        expr='aws_ec_key_type_based_latency_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="key-{{dimension_CacheClusterId}}",
                        refId='D',
                    ),
                    Target(
                        expr='aws_ec_sorted_set_based_latency_cmds_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="sorted_set-{{dimension_CacheClusterId}}",
                        refId='E',
                    ),
                    Target(
                        expr='aws_ec_set_based_cmds_latency_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="set_based-{{dimension_CacheClusterId}}",
                        refId='F',
                    ),
                    Target(
                        expr='aws_ec_hash_based_cmds_latency_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="hash-{{dimension_CacheClusterId}}",
                        refId='G',
                    ),
                    Target(
                        expr='aws_ec_list_based_cmds_latency_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="list-{{dimension_CacheClusterId}}",
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
                        expr='aws_ec_database_memory_usage_percentage_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="{{dimension_CacheClusterId}}",
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
                        expr='aws_ec_swap_usage_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="{{dimension_CacheClusterId}}",
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
                        expr='aws_ec_memory_fragmentation_ratio_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="{{dimension_CacheClusterId}}",
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
                        expr='aws_ec_curr_connections_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="{{dimension_CacheClusterId}}",
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
                        expr='aws_ec_new_connections_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="{{dimension_CacheClusterId}}",
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
                        expr='aws_ec_cache_hit_rate_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="{{dimension_CacheClusterId}}",
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
                        expr='aws_ec_cache_misses_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="{{dimension_CacheClusterId}}",
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
                        expr='aws_ec_curr_items_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="{{dimension_CacheClusterId}}",
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
                        expr='aws_ec_evictions_average{dimension_CacheClusterId=~"$Cluster"}',
                        legendFormat="{{dimension_CacheClusterId}}",
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