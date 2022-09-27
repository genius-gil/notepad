import re
from datetime import date, timedelta

# 삼성전자 재무제표 encparam, id 값 가져오기 : re 정규식 활용
# 삼성전자 cmp_cd : 005930
# url = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=005930"

fin = {}
samsung = """function getAddInfoData01(extY, extQ)
                {
                        var _freq_typ;
                        var _fin_typ;

                        switch($('#cTB00 .on').attr('id'))
                        {
                                case "cns_td20": _freq_typ = "A"; break;
                                case "cns_td21": _freq_typ = "Y"; break;
                                case "cns_td22": _freq_typ = "Q"; break;
                        }

                        switch($("#finGubun > option:selected").val())
                        {
                                case "MAIN" : _fin_typ = 0; break;
                                case "GAAPS": _fin_typ = 1; break;
                                case "GAAPL": _fin_typ = 2; break;
                                case "IFRSS": _fin_typ = 3; break;
                                case "IFRSL": _fin_typ = 4; break;
                        }
                        $.ajax({
                                url     : "ajax/cF1001.aspx",
                                async  : false,
                                type    : 'get',
                                dataType: 'html',
                                data: {
                                        cmp_cd    : '005930'
                , fin_typ : _fin_typ
                                , freq_typ: _freq_typ
                                , extY: extY
                , extQ: extQ
                , encparam: 'UStTUmgzQ0tvdWJwYy9MdHFicjdodz09'
                , id: 'RVArcVR1a2' ? 'RVArcVR1a2' : ''
                                },
                                success: function (data) {
                                        gtag('config', 'UA-74989022-7', {'page_path': '/company/ajax/cF1001.aspx'});
                                        $('#RVArcVR1a2').html(data);
                                        if(extQ==0)
                                        {
                                                $('.r02c07').addClass('endLine')
                                        }
                                        // 재무 컬럼 펼치기
                                        $('.btn_moreY').click(function(){
                                                if($(this).data('ext')==0){
                                                        getAddInfoData01(1, $('.btn_moreQ').data('ext'));
                                                        $(this).data('ext',1);
                                                }
                                                else{
                                                        getAddInfoData01(0, $('.btn_moreQ').data('ext'));
                                                        $(this).data('ext',0);
                                                }
                                        });
                                        $('.btn_moreQ').click(function(){
                                                if($(this).data('ext')==0){
                                                        getAddInfoData01($('.btn_moreY').data('ext'),1);
                                                        $(this).data('ext',1);
                                                }
                                                else{
                                                        getAddInfoData01($('.btn_moreY').data('ext'),0);
                                                        $(this).data('ext',0);
                                                }
                                        });
                                }
                        });
                }"""
pattern_enc = re.compile("encparam: '(.+)'", re.IGNORECASE)
pattern_id = re.compile("id: '(.+?)'", re.IGNORECASE)

result_enc = pattern_enc.search(samsung).groups()[0]
result_id = pattern_enc.search(samsung).groups()[0]

fin['encparam'] = result_enc
fin['id'] = result_id

print(fin)

print('-'*50)

# 날짜(일수) 계산 및 전개 연산자 : 리스트 기반
order_date = ['오늘', '어제', '그제', '지난주', '지난달', '6개월전']
print_date = []
for i in order_date:
    if i in '오늘':
        print_date.append(str(date.today()))
    elif i in '어제':
        print_date.append(str(date.today() - timedelta(days=1)))
    elif i in '그제':
        print_date.append(str(date.today() - timedelta(days=2)))
    elif i in '지난주':
        print_date.append(str(date.today() - timedelta(weeks=1)))
    elif i in '지난달':
        print_date.append(str(date.today() - timedelta(weeks=4)))
    elif i in '6개월전':
        print_date.append(str(date.today() - timedelta(weeks=4*6)))
print('오늘 : {}, 어제 : {}, 그제 : {}, 지난주 : {}, 지난달 : {}, 6개월전 : {}'.format(*print_date))
