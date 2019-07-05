from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.gateway.okex import OkexGateway

def main():
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)

    ok_gateway = main_engine.add_gateway(OkexGateway)
    ok_gateway.connect()
    print(u'服务启动成功')

if __name__ == "__main__":
    main()
