class SystemMonitor:
    def load_activity(self):
        """
        소스에서 처리할 이벤트 가져오기
        :return:
        """
        pass

    def identify_events(self):
        """
        가져온 이벤트를 파싱하여 도메인 객체 이벤트로 변환
        :return:
        """
        pass

    def stream_events(self):
        """
        파싱한 이벤트를 외부 에이전트로 전송
        :return:
        """
        pass
