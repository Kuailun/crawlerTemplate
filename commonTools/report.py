# -*- coding: utf-8 -*-
# @File: report.py
# @Author: Yuchen Chai
# @Date: 2021/6/21 14:19
# @Description:

from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class ReportProgress:
    def __init__(self, name):
        # You can generate a Token from the "Tokens Tab" in the UI
        self.token = "M-fxkRMFC1et1wYiWbgiqb6VSh5neFMpY2BzJZehhZs0Qk22ejhniNTK3t6tNiPPnRU6OTNSiIJchO0Rfx6_fw=="
        self.org = "ycchai14@gmail.com"
        self.bucket = "Scraper"
        self.host = name

        self.client = InfluxDBClient(url="https://us-central1-1.gcp.cloud2.influxdata.com", token=self.token)

    def report(self, item, key, value):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)

        data = f"mem,level_1={self.host},level_2={item} {key}={value}"
        write_api.write(self.bucket, self.org, data)

if __name__ == "__main__":
    report_progress = ReportProgress("weibo")
    report_progress.report("user","new_user",9)