# coding=utf-8
import json
import yaml
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class Filter:
    """
    Custom type used in Args
    """
    filter_value: str
    field_name: str
    filter_type: str


@dataclass
class Args:
    """
    Container for all request attributes 
    """
    metrics: List[str] = None
    data_level: str = None
    end_date: Optional[str] = None
    order_type: Optional[str] = None
    order_field: Optional[str] = None
    page_size: Optional[int] = None
    start_date: Optional[str] = None
    advertiser_id: str = None
    filters: Optional[List[Filter]] = None
    field_name: Optional[str] = None
    filter_type: Optional[str] = None
    service_type: str = None
    lifetime: bool = None
    report_type: str = None
    page: Optional[int] = None
    dimensions: List[str] = None

    def get_input_args(self):
        all_attrs = asdict(self)
        return {original_key: all_attrs[original_key] for original_key in all_attrs.keys()\
             if all_attrs[original_key]}
    
    def json(self):
        return json.dumps(self.get_input_args())


def parse_query_into_args() -> Args:
    """
    Parse arguments from query.yaml
    and return 
    """
    with open("./tonton_utils/query.yaml", "r") as y:
        query = yaml.safe_load(y)

    if query["filter_flag"]:
        return Args(
            metrics=query["metrics"],
            data_level=query["data_level"],
            end_date=query["end_date"],
            order_type=query["order_type"],
            order_field=query["order_field"],
            page_size=query["page_size"],
            start_date=query["start_date"],
            advertiser_id=query["advertiser_id"],
            filters=query["filters"],
            service_type=query["service_type"],
            lifetime=query["lifetime"],
            report_type=query["report_type"],
            page=query["page"],
            dimensions=query["dimensions"]
        )
    
    return Args(
            metrics=query["metrics"],
            data_level=query["data_level"],
            end_date=query["end_date"],
            order_type=query["order_type"],
            order_field=query["order_field"],
            page_size=query["page_size"],
            start_date=query["start_date"],
            advertiser_id=query["advertiser_id"],
            service_type=query["service_type"],
            lifetime=query["lifetime"],
            report_type=query["report_type"],
            page=query["page"],
            dimensions=query["dimensions"]
        )
    
