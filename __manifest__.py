{
    # Tên module
    'name': 'Tutorial Odoo 17.0',
    'version': '1.0',

    # Loại module
    'category': 'Tutorial',

    # Độ ưu tiên module trong list module
    # Số càng nhỏ, độ ưu tiên càng cao
    #### Chấp nhận số âm
    'sequence': 5,

    # Mô tả module
    'summary': 'Module này để các bạn khởi học và thực hiện các bước ban đầu để tạo module',
    'description': '',


    # Module dựa trên các category nào
    # Khi hoạt động, category trong 'depends' phải được install
    ### rồi module này mới đc install
    'depends': [],

    # Module có được phép install hay không
    # Nếu bạn thắc mắc nếu tắt thì làm sao để install
    # Bạn có thể dùng 'auto_install'
    'installable': True,
    'auto_install': False,
    'application': True,

    # Import các file cấu hình
    # Những file ảnh hưởng trực tiếp đến giao diện (không phải file để chỉnh sửa giao diện)
    ## hoặc hệ thống (file group, phân quyền)
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/course_list_template.xml',
        'views/menu_item_course.xml',
        'views/menu_item_lesson.xml',
        'views/menu_view.xml',
    ],

    # Import các file cấu hình (chỉ gọi từ folder 'static')
    # Những file liên quan đến
    ## + các class mà hệ thống sử dụng
    ## + các chỉnh sửa giao diện
    ## + t
    'assets': {
        'point_of_sale._assets_pos': [
            'hello_world/static/src/**/*'
        ],

    },
    'license': 'LGPL-3',
}
