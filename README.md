# rest-framework-djongo

`rest-framework-djongo` 是一个用于处理 Djongo（Django 和 MongoDB 的集成）相关序列化和视图操作的工具库，帮助开发者更方便地在 Django REST Framework 中使用 MongoDB。

## 项目信息

- **项目名称**：rest-framework-djongo
- **版本**：0.1.2
- **作者**：vfeng <1914007838@qq.com>
- **Python 版本要求**：>=3.9

## 功能概述

### 序列化器
- **GenericDjongoSerializer**：为 `GenericDjongoModel` 提供序列化功能，映射了多种 Django 模型字段到 Django REST Framework 的字段。
- **EmbeddedSerializer**：用于处理嵌入式数据的序列化，继承自 `GenericDjongoSerializer`，并跳过了一些验证器。

### 字段
- **ObjectIdField**：处理 MongoDB 的 `ObjectId` 类型数据，提供了 `to_internal_value` 和 `to_representation` 方法。
- **EmbeddedField**：处理嵌入式字段，也提供了 `to_internal_value` 和 `to_representation` 方法。

### 视图
- **GenericAPIView**：继承自 `drf_generics.GenericAPIView`，提供了 `get_object` 方法用于获取对象。

## 安装

该项目使用 Poetry 进行依赖管理，确保你已经安装了 Poetry（https://python-poetry.org/docs/#installation）。

克隆项目到本地：

```bash
git clone <项目仓库地址>
cd rest-framework-djongo