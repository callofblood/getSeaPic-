function fileImport() {
    //获取读取我文件的File对象
    localStorage.removeItem('newCodes');
    var selectedFile = document.getElementById('files').files[0];
    var name = selectedFile.name; //读取选中文件的文件名
    var size = selectedFile.size; //读取选中文件的大小
    console.dir("文件名:" + name + "大小:" + size);
    var reader = new FileReader(); //这是核心,读取操作就是由它完成.
    reader.readAsText(selectedFile); //读取文件的内容,也可以读取文件的URL
    reader.onload = function () {
        codes = this.result
        reg = /case (\d{2})/
        temp = codes.split('\n')
        for (var i = 0; i < temp.length; i++) {
            if (temp[i].match(reg)) {
                console.log(temp[i].match(reg)[1])
                picNum = temp[i].match(reg)[1]
                break
            }
        }
        document.getElementById("code").value = codes
        $('#mapid').val(picNum)
        code = document.getElementById("code").value

    }
}